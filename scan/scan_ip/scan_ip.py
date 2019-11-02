#!/usr/bin/python3
# -*- coding=utf8 -*-
"""
# @Author : pig
# @CreatedTime:2019-10-3123:46:56
# @Description : 
"""

import os
import optparse
import math
import threading
import pysnooper

parser = optparse.OptionParser()
parser.usage = "scan_ip1.py -i ip -b begin_ip -e end_ip"
parser.add_option("-i", "--ip", dest = "ip", help = "ip to test", action = "store", type = "string", metavar = "IP")
parser.add_option("-b", "--begin_ip", dest = "begin_ip", help = "begin_ip to test", action = "store", type = "string", metavar = "BEGINIP")
parser.add_option("-e", "--end_ip", dest = "end_ip", help = "end_ip to test", action = "store", type = "string", metavar = "ENDIP")
parser.add_option("-t", "--threads", dest = "threads", help = "num of threads", action = "store", type = "string", metavar = "THREADS")
(options, args) = parser.parse_args()

temp_ip = options.ip
begin_ip = options.begin_ip
end_ip = options.end_ip
ths = int(options.threads)

temp_ip_list = []
final_ip_list = []
ip_list = range(int(begin_ip), int(end_ip) + 1)
ip_num = len(ip_list)
result_num = math.ceil(ip_num / ths)
flag = 0
for line in ip_list:
	flag += 1
	ip = temp_ip + str(line)
	temp_ip_list.append(ip)
	if flag == result_num:
		flag = 0
		final_ip_list.append(temp_ip_list)
		temp_ip_list = []
final_ip_list.append(temp_ip_list)

# @pysnooper.snoop()
def scan(thread_ip_list):
	for ip in thread_ip_list:
		cmd = "ping -c 6 " + str(ip)
		# print (cmd)
		ping = os.popen(cmd).read()
		if "ttl" in ping:
			print ("ip is alive: " + str(ip))
		else:
			continue

ths_list = []
for thread_ip_list in final_ip_list:
	ths_list.append(threading.Thread(target = scan, args = (thread_ip_list, )))
for th in ths_list:
	th.start()


