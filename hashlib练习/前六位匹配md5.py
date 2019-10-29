import hashlib

known_md5 = input("请输入数字加密后的md5值：")
known_mingwen = range(1000,1000000)
for s in known_mingwen:
	md5 = hashlib.md5()
	md5.update(str(s).encode("utf-8"))
	en_pd = md5.hexdigest()
	# print (en_p)
	if en_pd[0:6] == known_md5:
		print (known_md5, s)
		break
	else:
		continue
print ("该md5加密值不在",known_mingwen)
