def yuan(name):
	name2 = int(name[4:6])
	name3 = int(name[6:9])
	s_um = 0
	if name2 == 1:
		s_um = s_um + name3
	elif name2 == 2:
		s_um = s_um + 31 + name3
	elif name2 == 3:
		s_um = s_um + 31 + 28 +name3
	elif name2 == 4:
		s_um = s_um + 31 + 28 + 31 + name3
	elif name2 == 5:
		s_um = s_um + 31 + 28 + 31 + 30 + name3
	elif name2 == 6:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + name3
	elif name2 == 7:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + 30 + name3
	elif name2 == 8:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + 30 + 31 + name3
	elif name2 == 9:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + name3
	elif name2 == 10:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + name3
	elif name2 == 11:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + name3
	elif name2 == 12:
		s_um = s_um + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + name3
	return s_um
name = input("输入年月日")
name1 = int(name[0:4])
name2 = int(name[4:6])
name3 = int(name[6:9])
if len(name) == 8 and name2 >= 1 and name2 <= 12 and name3 >= 0 and name3 <=31:
	if (name1%4 == 0 and name1%100 != 0) or name1%400 == 0:
		k = yuan(name)
		print("一年第%d天"%k)
	else:
		k = yuan(name) - 1
		print("一年第%d天"%k)
else:
	print("输入格式不对")
