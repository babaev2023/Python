from pytube import YouTube



URL = 'https://www.youtube.com/watch?v=Iv5-5R5jxCw'
DOWNLOAD_DIR = 'Downloads'

def download_video(url):
    yt = YouTube(url)
    #for stream in yt.streams:
       # print(stream)
    yt.streams.get_highest_resolution().download(DOWNLOAD_DIR)



if __name__ == '__main__':
    download_video(URL)

