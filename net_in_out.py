import sys
import time


# Real-time monitoring of interface 
if len(sys.argv) > 1:
    interface = sys.argv[1]
else:
    interface = 'eth0'
print('Interface:{}'.format(interface))

def traffic():
    # network file
    with open('/proc/net/dev') as f:
        data = f.readlines()
        for line in data:
            if interface in line:
                stats.append([float(line.split()[1]),float(line.split()[9])])

while True:
    stats = []
    traffic()
    time.sleep(1)
    traffic()
    IN = round((stats[1][0] - stats[0][0])/1024/1024,3)
    OUT = round((stats[1][1] - stats[0][1])/1024/1024,3)
    print("NET_IN:{}\t\tNET_OUT:{}".format(IN,OUT))
    stats.clear()
