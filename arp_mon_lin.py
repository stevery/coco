import subprocess
from time import sleep

counter = 0
arp_table = {}

while True:
    arp_r = subprocess.check_output(["arp","-a"],
                                    stderr=subprocess.STDOUT,
                                    shell=True)
    arp_r = arp_r.split('\n')[1:-1]
    for line in arp_r:
        tmp = line.split()
        if tmp[2] in arp_table:
            if tmp[0] != arp_table[tmp[2]]:
                print "found arp spoofing"
                print "original: {} {}".format(tmp[2], arp_table[tmp[2]])
                print "spoofing: {} {}".format(tmp[2], tmp[0])
        else:
            arp_table[tmp[2]] = tmp[0]
    
    sleep(30)
    if counter % 5:
        for line in arp_table:
            print line, arp_table
    counter += 1
