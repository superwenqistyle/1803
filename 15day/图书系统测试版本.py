cards=[]
#打印菜单
def print_menu():
	print("欢迎进入图书系统".center(30,"*"))
	print("1.借阅登记".center(30," "))
	print("2.查询记录".center(30," "))
	print("3.修改记录".center(30," "))
	print("4.删除记录".center(30," "))
	print("5.退阅登记".center(30," "))
	print("6.打印记录".center(30," "))
	print("7.退出系统".center(30," "))
#分发功能模块
def input_function():
	while True:
		in_put = int(input("请选择功能:"))
		if in_put == 1:
			add_card()
		elif in_put == 2:
			find_card()
		elif in_put == 3:
			modify_card()
		elif in_put == 4:
			del_card()
		elif in_put == 5:
			debook_card()
		elif in_put == 6:
			print_card()
		else:
			break
def save_card():
	f = open("cards.data","w")
	f.write(str(cards))
	f.close()
def open_card():
	global cards
	try:
		with open("cards.data") as f_obj:
			cards = eval(f_obj.read())
		f_obj.close()
	except FileNotFoundError:
		print("")
#借阅模块
def add_card():
	card={}
	flag = 0  #默认card库不存在
	id_number = int(input("请输入本人身份证号"))
	for temp in cards:
		if id_number == temp["id_number"]:
			flag = 1
			print("已达借阅上限,请及时还书")
	if flag == 0:
		name = input("请输入姓名")
		number = int(input("请输入学号"))
		profession = input("请输入专业")
		booklist = input("请输入借阅书目")
		debook = "True"
		card["id_number"]=id_number
		card["name"]=name
		card["number"]=number
		card["profession"]=profession
		card["booklist"]=booklist
		card["debook"]=debook
		cards.append(card)
		save_card()
		print("借阅登记成功")
def find_card():
	id_number = int(input("请输入要查找的身份证号"))
	flag = 0
	for temp in cards:
		if id_number == temp["id_number"]:
			flag = 1
			print("姓名:%s\t身份证号码:%d\t学号:%d\t专业:%s\t书目:%s"%(temp["name"],temp["id_number"],temp["number"],temp["profession"],temp["booklist"]))
	if flag == 0:
		print("查无此人信息")
def modify_card():
	id_number = int(input("请输要修改的身份证号"))
	flag = 0
	for temp in cards:
		if id_number == temp["id_number"]:
			flag = 1
			option = int(input("请选择要修改的内容: 1.姓名 2.学号 3.专业 4.书目"))
			if option == 1:
				name = input("输入新的姓名")
				temp["name"]=name
			elif option == 2:
				number = int(input("输入新的学号"))
				temp["number"]=number
			elif option == 3:
				profession = input("输入新的的专业")
				temp["profession"]=profession
			elif option == 4:
				booklist = input("输入新的书目")
			else:
				print("输入格式错误")
			save_card()
	if flag == 0:
		print("暂无此人信息")

def del_card():
	id_number = int(input("输入要删除的身份证号"))
	flag = 0
	for temp in cards:
		if id_number == temp["id_number"]:
			flag = 1
			cards.remove(temp)
			print("信息移除成功")
			save_card()
	if flag == 0:
		print("暂无此人信息")
def debook_card():
	id_number = int(input("输入身份证号"))
	flag = 0
	for temp in cards:
		if id_number == temp["id_number"]:
			flag = 1
			debook = input("输入退阅书目")
			temp["debook"]=debook
			print("退阅成功")
			
	if flag == 0:
		print("身份证号错误")
def print_card():
	if cards == []:
		print("记录为空")
	else:
		for temp in cards:
			print("姓名:%s\t身份证号码:%d\t学号:%d\t专业:%s\t书目:%s"%(temp["name"],temp["id_number"],temp["number"],temp["profession"],temp["booklist"]))


print_menu()
open_card()
input_function()



