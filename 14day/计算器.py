def computer(a,b,c):
	if c == 1:
		k = a+b
		print("和:%0.2f"%k)
	elif c == 2:
		k = a-b
		print("差:%.02f"%k)
	elif c == 3:
		k = a*b
		print("积:%.02f"%k)
	elif c == 4:
		if b != 0:
			k = a/b
			print("商:%.02f"%k)
		else:
			print("输入格式不对")
a = float(input("输入一个数"))
b = float(input("再输入一个数"))
c = int(input("输入运算符号: 1.和 2.差 3.乘 4.商"))
computer(a,b,c)	
