s_sum = 0
for i in range(1,13):  #月份
	if i == 1 or i == 12:
		d = 32
	elif i == 2 or i == 11:
		d = 18
	elif i == 3 or i == 10:
		d = 7
	elif i == 4 or i == 9:
		d = 80
	elif i == 5 or i == 8:
		d = 34
	elif i == 6 or i == 7:
		d = 70

	if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
		t = 31
	elif i == 4 or i == 6 or i == 9 or i == 11:
		t = 30
	else:
		t = 28
	sum = 0
	for r in range(1,2*t+1):
		if d <= 6:
			m = 3
		elif d > 6 and d <= 12:
			m = 4
		elif d > 12 and d <=22:
			m = 5
		elif d > 22 and d <= 32:
			m = 6
		else:
			if (d-32)%20 == 0:
				m = (d-32)/20 + 6
			else:
				m = int((d-32)/20) + 7
	
		if sum > 100 and sum <= 150:
			m = 0.8*m
		elif sum > 150 and sum <= 400:
			m = 0.5*m
		sum += m
	print("第%d月花费%.02f"%(i,sum))
	s_sum += sum
print(s_sum)
