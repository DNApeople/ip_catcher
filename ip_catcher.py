import subprocess,re
O_put=subprocess.run(["ipconfig"], capture_output=True).stdout.decode() 
ip4=(re.findall("IPv4 Address. . . . . . . . . . . :(.*)\r",O_put))
ip6=(re.findall("IPv6 Address. . . . . . . . . . . :(.*)\r",O_put))
np=(re.findall("Unknown adapter(.*)\r",O_put))




ALL = []

if len(ip6) !=0:
    global i6
    i6 = format(str(ip6))
    print('\n' , i6)
    ALL.append(i6)
    

else:
    global n6
    n6 = ("no ipV6 addres.\n")
    print(n6)
    ALL.append(n6)
    

print(ip4,'\n')
ALL.append(ip4)

if len(ip4) > 1:
    global pos
    pos = ("posibile one IP belong to one of "+ str(np))
    print(pos)
    ALL.append(pos)

else:
    d=0

with open('ip.txt', 'w+') as f:
    for items in ALL:
        f.write('%s\n' %items)
        print("\nsaved")
    f.close()

exit()