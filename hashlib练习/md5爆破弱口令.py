# conding:utf-8
#! /bin/bash/python3
import hashlib

def ruo_md5():
    text = open("password.txt").read()
    ruokou = text.splitlines(s)
    # print (ruokou)
    for s in ruokou:
    #     print (s)
        md5 = hashlib.md5()
        md5.update(bytes(s, encoding="utf-8"))
        en_pd = md5.hexdigest()
        print ("{:>16}".format(s),":",en_pd)

def de_md5(known_md5):
    text = open("password.txt").read()
    ruokou = text.split("\n")
    # print (ruokou)
    for s in ruokou:
    #     print (s)
        md5 = hashlib.md5()
        md5.update(bytes(s, encoding="utf-8"))
        en_ruopd = md5.hexdigest()
        if known_md5 == en_ruopd:
            print ("密文".rjust(len(known_md5), " "),":","明文".ljust(len(s)))
            print (known_md5,":","{:<16}".format(s),)
            break
        else:
            continue
        print ("该md5值不在本人字典里")
    
def en_md5(pd):
#     pd = input("输入想要md5加密的密码:")    
    md5 = hashlib.md5()
    md5.update(pd.encode("utf-8"))
    en_pd = md5.hexdigest()
    print ("明文".rjust(16, " "), ":", "密文".ljust(len(en_pd), " "))
    print ("{:>16}".format(pd),":",en_pd)

    
if __name__ == "__main__":
#     ruo_md5() # 要打印的弱口令md5值
    # known_md5 = input("请输入已知弱口令的md5值:")
    # de_md5(known_md5) # 这两行，解密md5值
    pd = input("请输入想要md5加密的密码:")
    en_md5(pd) # 这两行进行md5加密
