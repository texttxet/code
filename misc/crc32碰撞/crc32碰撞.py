import string
import zipfile
import binascii

def jisuancrc(crc):
	for a in dic:
		for b in dic:
			for c in dic:
				for d in dic:
					s = a + b + c + d
					s = str(s).encode()
					# print(type(s))
					
					if (binascii.crc32(s)) == crc:
						print(s)
						# print(binascii.crc32(s))
						return

def getcrc():
	f = zipfile.ZipFile("flag.zip", "r")
	GetCrc = f.getinfo("flag.txt")
	crc = GetCrc.CRC
	print(hex(crc))
	jisuancrc(crc)

dic = "abcdefghijklmnopqrst1234567890" # 可以自己自定义文件内容范围可打印字符
# dic = string.ascii_letters + string.digits # 直接应用模块来确定文件内容范围
getcrc()
