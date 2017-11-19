#-*- encoding:utf8 -*-

import subprocess
import re
from time import sleep


while True:
    arp_r = subprocess.check_output(["arp","-a"],
                                    stderr=subprocess.STDOUT,
                                    shell=True)

    my_arp = {}

    a = arp_r.split('\r\n\r\n')
    for i in a:
        tmp_list =  i.strip().split('\r\n')
        if re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", tmp_list[0]):
            tmp_interface = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", tmp_list[0]).group()
            my_arp[tmp_interface] = {}
            for j in tmp_list[2:]:
                try:
                    tmp_body = j.strip().split()
                    if tmp_body[1] in my_arp[tmp_interface]:
                        print 'arp spoofing found {}:{}'.format(tmp_body[0],tmp_body[1])
                        print my_arp[tmp_interface][tmp_body[1]]
                    else:
                        my_arp[tmp_interface].update({tmp_body[1]:tmp_body[0]})
                except:
                    pass

    sleep(30)