cards=[]
def print_menu():
	print("学生成绩管理系统".center(60,"*"))
	print("1.录入成绩".center(60," "))
	print("2.修改成绩".center(60," "))
	print("3.打印成绩".center(60," "))
	print("4.查询成绩".center(60," "))
	print("5.删除成绩".center(60," "))
	print("6.退出系统".center(60," "))
def input_function():
	while True:
		function = int(input("请选择功能:"))
		if function == 1:
			add_card()
		elif function == 2:
			update_card()
		elif function == 3:
			print_card()
		elif function == 4:
			find_card()
		elif function == 5:
			del_card()
		else:
			break
def add_card():
	print("录入成绩".center(60,"*"))
	card={}
	num = int(input("请输入学号"))
	flag=0 #默认成绩库不存在
	for temp in cards:
		if temp["num"] == num:
			flag = 1
			print("输入学号重复")
	if flag == 0:
		name = input("输入姓名")
		math = float(input("请输入数学成绩"))
		English = float(input("请输入英语成绩"))
		card["num"]=num
		card["name"]=name
		card["math"]=math
		card["English"]=English
		cards.append(card)
		print("成绩录入成功")
def update_card():
	print("修改成绩".center(60,"*"))
	flag = 0  #默认不在
	#def xiugai():
	num = int(input("输入要修改的学号"))
	for temp in cards:
		if num == temp["num"]:
			flag = 1
			xuan = int(input("请输入要修改的成绩: 1.math 2.English"))
			if xuan == 1:
				math = float(input("输入要修改后的成绩"))
				temp["math"]=math
			elif xuan == 2:
				English =float(input("输入要修改后的成绩"))
				temp["English"]=English
			print("修改成功")
	if flag == 0:
		print("学号不存在")
def print_card():
	print("打印成绩".center(60,"*"))
	for temp in cards:
		print("学号:%d\t姓名:%s\t数学:%.02f\t英语:%.02f"%(temp["num"],temp["name"],temp["math"],temp["English"]))
def find_card():
	print("查询成绩".center(60,"*"))
	num = int(input("输入要查找的学号"))
	flag = 0 #默认不存在
	for temp in cards:
		if num == temp["num"]:
			flag = 1
			print("学号:%d\t姓名:%s\t数学:%.02f\t英语:%.02f"%(temp["num"],temp["name"],temp["math"],temp["English"]))
	if flag == 0:
		print("查找学号不存在")
def del_card():
	print("删除成绩".center(60,"*"))
	num = int(input("输入要删除成绩的学号"))
	flag = 0
	for temp in cards:
		if num == temp["num"]:
			flag = 1
			cards.remove(temp)
	if flag == 0:
		print("对象不存在")
print_menu()
input_function()

