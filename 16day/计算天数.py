def day(date):
	all_day = 0
	date0 = int(date)
	date1 = int(date[0:4])
	date2 = int(date[4:6])
	date3 = int(date[6:])
	flag = 0 #默认平年
	if (date0%4 == 0 and date0%100 != 0) or date0%400 == 0:
		flag = 1
		big_month = [1,3,5,7,8,10,12]
		small_month = [4,6,9,11]
	#if flag = 1:
	for i in range(1,date2):
		if i in big_month:
			all_day+=31
		elif i in small_month:
			all_day+=30
		elif i == 2 and falg == 1:
			all_day+=29
		elif i == 1 and flag == 0:
			all_day+=28
	all_day+=date3
	print("一年第%d天"%all_day)
date = input("输入年份日期")
day(date)
