print("名片v1.0测试系统".center(60,"*"))
print("名片系统功能".center(60,"*"))
print(" 1.新增名片 ".center(60,"*"))
print(" 2.查找名片 ".center(60,"*"))
print(" 3.修改名片 ".center(60,"*"))
print(" 4.删除名片 ".center(60,"*"))
print(" 5.遍历名片 ".center(60,"*"))
print(" 6.退出名片 ".center(60,"*"))
cards=[]  #名片库
while True:
	function = int(input("选择要执行的功能: 1.新增名片 2.查找名片 3.修改名片 4.删除系统 5.遍历名片 6.退出系统"))
	if function == 1:
		print("新增名片".center(60,"*"))
		flag=0  #假设默认名片库不存在
		card={}  #个人信息库
		phone = input("请输入新的电话")
		if phone.isdigit() == True and phone.startswith("1") == True and len(phone) == 11:
			#print("数字")
			#if phone.startswith("1") == True:
			#	if len(phone) == 11:
			isdelete = o  #默认		
	elif function == 2:
		print("查找名片".center(60,"*"))
	elif function == 3:
		print("修改名片".center                                                                                                                    (60,"*"))
	elif function == 4:
		print("删除名片".center(60,"*"))
	elif function == 5:
		print("遍历名片".center(60,"*"))
	elif function == 6:
		print("退出系统".center(60,"*"))

