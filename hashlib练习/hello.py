import hashlib
 
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    print(m.hexdigest())
    return m.hexdigest()
 
def md5GBK(str1):
    m = hashlib.md5(str1.encode(encoding='gb2312'))
    print(m.hexdigest())
    return m.hexdigest()
 
md5('QNKCDZO')
md5GBK('你好')