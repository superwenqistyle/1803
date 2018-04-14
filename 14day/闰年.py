def year(y):
	if (y%4 == 0 and y%100 != 0) and y%400 == 0:
		print("闰年")
	else:
		print("平年")
t = int(input("输入年份:"))
year(t)
