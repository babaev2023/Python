import network
 
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlans = wlan.scan()             # scan for access points
 
for i in wlans:
    print(i)