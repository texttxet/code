import getopt
import sys
import math
import threading
import requests

def banner():
    print ("*" * 57)
    print ("*" * 3 + " " * 19 + "DirBrute v 1.0" + " " * 18 + "*" * 3)
    print ("*" * 3 + " " * 12 + "This tool just develop fun!" + " " * 12 + "*" * 3)
    print ("*" * 57)

# python Dirbrute.py -u url -t thread -d dictionary

def usage():
    print ("*" * 57)
    print ("*" * 3 + " " * 13 + "This is the tool's usage" + " " * 14 + "*" * 3)
    print ("*" * 3 + "python Dirbrute.py -u url -t threads -d dictionary!" + "*" * 3)
    print ("*" * 57)


def start():
    if len(sys.argv) == 7:
        # This is true length
        opts, args = getopt.getopt(sys.argv[1:], "u:t:d:")
        for k, v in opts:
            if k == "-u":
                url =v
            elif k == "-t":
                threads = v
            elif k == "-d":
                dic = v
        multi_scan(url, threads, dic)
    else:
        print ("Error Argument!")
        sys.exit()

def multi_scan(url,threads,dic):
    # 第一步读字典文件
    # 第二步 确定读取的行数 len(dic_list) / threads 向上去取整
    # 第三步 确定每个线程读取的列表[[t1],[t2],[t3],...]
    result_list = []
    threads_list = []
    with open(dic, "r") as f:
        dic_list = f.readlines()
        if len(dic_list) % int(threads) == 0:
            thread_read_line_num = len(dic_list) / int(threads)
        else:
            thread_read_line_num = math.ceil(len(dic_list) / int(threads))
        i = 0
        temp_list = []
        for line in dic_list:
            i += 1
            if i % thread_read_line_num == 0:
                temp_list.append(line.strip())
                result_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(line.strip())
    for i in result_list:
        # print (i)
        threads_list.append(threading.Thread(target = scan, args = (url,i)))
    for t in threads_list:
        t.start()

def scan(url, dic):
    # 实现扫描功能 requests
    for line in dic:
        r = requests.get(url = url + '/' + line)
        if r.status_code == 200 or r.status_code == 302:
            print (r.url + " : " + str(r.status_code))


banner()
usage()
start()