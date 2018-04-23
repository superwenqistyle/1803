accounts=[]  #注册用户库
def print_system():
	print("账号管理系统".center(30,"*"))
	print("系统功能如下:".center(30," "))
	print("1.账号注册".center(30," "))
	print("2.账号登录".center(30," "))
	print("3.退出系统".center(30," "))
def function():
	while True:
		print_system()
		number = int(input("请输入功能选项:"))
		if number == 1:
			account_card()
		elif number == 2:
			login_card()
		else:
			break
def account_card():
	account = input("输入账号")
	passwd = int(input("输入密码"))
	flag=0  #默认账号不存在
	for temp in accounts:
		if account == temp["account"]:
			flag = 1
			print("账号已存在,注册不成功")
	if flag == 0:
		card={}
		card["account"]=account
		card["passwd"]=passwd
		card["status"]=0
		accounts.append(card)
		print("注册成功")
def login_card():
	account = input("请输入账户")
	passwd = int(input("请输入密码"))
	flag=0
	status = 0  #默认未登录
	for temp in accounts:
		if account == temp["account"]:
			if temp["status"] == 1:
				print("账号已登录")
			else:
				if passwd == temp["passwd"]:
					temp["status"]=1
					print("账户登录成功")
				else:
					print("密码错误")
			flag = 1
	if flag == 0:
		print("账号未注册")
def loginout():
	account = input("输入账号")
	passwd = int(input("输入密码"))
	for temp in accounts:
		if account == temp["account"]:
			pass
function()
		
	
	
	
	
