import re
import socket
import sys
import io


class MicroPyServer(object):

    def __init__(self, host="0.0.0.0", port=80):
        """ Constructor """
        self._host = host
        self._port = port
        self._routes = []
        self._connect = None
        self._on_request_handler = None

    def start(self):
        """ Start server """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self._host, self._port))
        sock.listen(1)
        while True:
            try:
                self._connect, address = sock.accept()
                request = self._get_request()
                if len(request) == 0:
                    self._connect.close()
                    continue
                if self._on_request_handler:
                    if not self._on_request_handler(request, address):
                        continue
                route = self.find_route(request)
                if route:
                    params = self._parse_params(request)
                    route["handler"](request, params)
                else:
                    self.not_found()
            except Exception as e:
                    self.internal_error(e)
            finally:
                self._connect.close()

    def add_route(self, path, handler, method="GET"):
        """ Add new route  """
        self._routes.append({"path": path, "handler": handler, "method": method})

    def send(self, response, status=200, content_type="Content-Type: text/plain", extra_headers=[]):
        """ Send response to client """
        if self._connect is None:
            raise Exception("Can't send response, no connection instance")

        status_message = {200: "OK", 400: "Bad Request", 403: "Forbidden", 404: "Not Found",
                          500: "Internal Server Error"}
        self._connect.sendall("HTTP/1.0 " + str(status) + " " + status_message[status] + "\r\n")
        self._connect.sendall(content_type + "\r\n")
        for header in extra_headers:
            self._connect.sendall(header + "\r\n")
        self._connect.sendall("X-Powered-By: MicroPyServer\r\n")
        self._connect.sendall("\r\n")
        self._connect.sendall(response)

    def find_route(self, request):
        """ Find route """
        lines = request.split("\r\n")
        method = re.search("^([A-Z]+)", lines[0]).group(1)
        path = re.search("^[A-Z]+\\s+(/[-a-zA-Z0-9_.]*)", lines[0]).group(1)
        for route in self._routes:
            if method != route["method"]:
                continue
            if path == route["path"]:
                return route
            else:
                match = re.search("^" + route["path"] + "$", path)
                if match:
                    print(method, path, route["path"])
                    return route

    def not_found(self):
        """ Not found action """
        self.send("404", status=404)

    def internal_error(self, error):
        """ Catch error action """
        output = io.StringIO()
        sys.print_exception(error, output)
        str_error = output.getvalue()
        output.close()
        self.send("Error: " + str_error, status=500)

    def on_request(self, handler):
        """ Set request handler """
        self._on_request_handler = handler

    def _get_request(self):
        """ Return request body """
        return str(self._connect.recv(4096), "utf8")

    def _parse_params(self, request):
        params = dict()

        try:
            lines = request.split("\r\n")
            params_string = re.search("\?([-a-zA-Z0-9_.=&%]+)\\sHTTP", lines[0]).group(1)
            params_pf = params_string.split("&")

            for i in params_pf:
                temp = i.split("=")
                params[temp[0]] = temp[1]
        except Exception as e:
            pass
    
        return params
