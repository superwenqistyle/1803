def tianshu(num):
	list=[0,30,28,31,30,31,30,31,31,30,31,30,31]
	num2 = int(num[4:6])
	num3 = int(num[6:9])
	s_um = 0
	for i in range(0,num2):
		s_um = s_um + list[i]
	s_um = s_um + num3
while True:
	num = input("输入年份日期")
	num1 = int(num[0:4])
	num2 = int(num[4:6])
	num3 = int(num[6:9])
if len(name) == 8 and name2 <= 12 and name3 <=31:
	if (num1%4 == 0 and num1%100 != 0) or num1%400 == 0:
		k = tianshu(num)
		print("一年第%d天"%k)
	else:
		k = tianshu(num) + 1
		print(k)
else:
	print("输入格式不合理")













