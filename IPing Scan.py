import subprocess
print('\x1b[0;31;47m'+"Devlopped By KANNOUN"+'\x1b[0m')
# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

ip = str(input("Type network Prefix (ex: 192.168.1): "))
print('\x1b[7;30;47m'+"Your Network Prefix is "+ip+'\x1b[0m')
start = int(input("First IP is: "+ip+"."))
stop1 = int(input("Last IP is: "+ip+"."))
stop2 = stop1 +1
print("Start Scanning!")
for ping in range(start,stop2):
    add = str(ip+"."+str(ping))
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', add], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    print ("Progress "+str(ping)+"/"+str(stop1), end="\r")
    if "Destination host unreachable" in output.decode('utf-8'):
        pass
    elif "Request timed out" in output.decode('utf-8'):
        pass
    elif "TTL expired in transit" in output.decode('utf-8'):
        pass
    else:
        print('\x1b[6;30;42m'+str(add), "is Online"+'\x1b[0m')
print('\x1b[4;36;40m'+"Scanning is Done for "+ip+"."+"["+str(start)+"-"+str(stop1)+"]"+'\x1b[0m')
input("Press enter to exit")