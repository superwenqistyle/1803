def number(phone):
	if phone.startswith("1") == True and len(phone) == 11:
		return True
	else:
		return False
phone = input("输入电话号码")
t = number(phone)
if t == False:
	print("输入电话错误")

phone1 = input("输入电话号码")
h = number(phone1)
if h == False:
	print("输入电话错误")
