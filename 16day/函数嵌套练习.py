def register(phone,passwd):
	result = isphone(phone)
	if result:
		print("注册成功")
	else:
		print("注册失败")
def login(phone,passwd):
	result = isphone(phone)
	if result:
		print("登录成功")
	else:
		print("登录失败")
def isphone(phone):
	if phone.startswith("1") == True and len(phone) == 11:
		return True
	else:
		return False
register("12345678901","12345678901")
login("12345678901","12345678901")
