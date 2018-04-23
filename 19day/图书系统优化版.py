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
		print_menu()
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
#数据存储模块
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
		print(" ")
#输入模块
def input_fun():
	id_number = int(input("输入身份证号"))
	return id_number
#判断模块
def check_test(id_number):
	flag=0
	for temp in cards:
		if id_number == temp["id_number"]:
			return temp
	if flag == 0:
		return None
#借阅模块
def add_card():
	id_number = input_fun()
	temp = check_test(id_number)
	if temp != None:
		print("已借阅，请及时还书")
	else:
		card={}
		name = input("请输入姓名")
		number = int(input("请输入学号"))
		profession = input("请输入专业")
		booklist = input("请输入借阅书目")
		debook = 1  #默认没有退还
		card["id_number"]=id_number
		card["name"]=name
		card["number"]=number
		card["profession"]=profession
		card["booklist"]=booklist
		card["debook"]=1  #借阅未还
		print("姓名:%s\t身份证号码:%d\t学号:%d\t专业:%s\t书目:%s"%(card["name"],card["id_number"],card["number"],card["profession"],card["booklist"]))
		#print(card)
		cards.append(card)
		save_card()
		print("借阅成功")
#信息查找模块
def find_card():
	id_number = input_fun()
	temp = check_test(id_number)
	if temp != None:
		if temp["debook"] == 1:
			print("书籍未归还")
		else:
			print("书籍已归还")
			#flag = 1
		print("姓名:%s\t身份证号码:%d\t学号:%d\t专业:%s\t书目:%s"%(temp["name"],temp["id_number"],temp["number"],temp["profession"],temp["booklist"]))
	else:
		print("查无此人借书信息")
#信息修改模块
def modify_card():
	id_number = input_fun()
	temp = check_test(id_number)
	if temp != None:
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
	else:
		print("暂无此人借书信息")
#信息删除模块
def del_card():
	id_number = input_fun()
	temp = check_test(id_number)
	if temp != None:
		cards.remove(temp)
		print("信息移除成功")
		save_card()
	else:
		print("暂无此人信息")
#退阅登记模块
def debook_card():
	id_number = input_fun()
	temp = check_test(id_number)
	if temp != None:
		temp["debook"]=0
		save_card()
		print("退阅成功")
	else:
		print("身份证号不存在")
#打印借书记录模块
def print_card():
	print("请选择功能: 1.打印全部　2.打印个人借书记录")
	choice = int(input("请选择功能"))
	if choice == 1:
		if cards == []:
			print("暂无记录")
		else:
			for temp in cards:
				print("姓名:%s\t身份证号码:%d\t学号:%d\t专业:%s\t书目:%s"%(temp["name"],temp["id_number"],temp["number"],temp["profession"],temp["booklist"]))
	elif choice == 2:
		id_number = int(input("输入要打印人的身份证号"))
		for temp in cards:
			if temp["id_number"] == id_number:
				print("姓名:%s\t身份证号码:%d\t学号:%d\t专业:%s\t书目:%s"%(temp["name"],temp["id_number"],temp["number"],temp["profession"],temp["booklist"]))
open_card()
input_function()
