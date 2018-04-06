d = int(input("请输入每天的距离"))
t = int(input("请输入每月的天数"))
sum = 0
for i in range(1,2*t):  #while i <= 2*t:
	if d <= 6:
		m = 3
	elif d > 6 and d <=12:
		m = 4
	elif d > 12 and d <= 22:
		m = 5
	elif d >22 and d <=32:
		m = 6
	else:
		if (d-32)%20 == 0:
			m = int((d-32)/20) + 6
		else:
			m = int((d-32)/20) + 7

	if sum > 100 and sum <= 150:
		m = 0.8*m
	elif sum > 150 and sum <= 400:
		m = 0.5*m
	print("第%d次花费%d元"%(i,m))  #i+=1
	sum = sum + m
print("总数%.02f元"%sum)
