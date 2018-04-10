print("名片系统".center(30,"*"))
print("1.新增名片".center(30,"*"))
print("2.查找名片".center(30,"*"))
print("3.修改名片".center(30,"*"))
print("4.删除名片".center(30,"*"))
cards=[]
while True:
	function = int(input("请选择功能选项: 1.新增 2.查找 3.修改 4.删除"))
	if function == 1:
		print("新增名片")
		flag = 0  #card库不存在
		card={}
		name = input("请输入名字")
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				break
		if flag == 1:
			print("名字重复,请重新输入")	
			continue
		job = input("输入工作")
		phone = int(input("输入电话号码"))
		company = input("输入公司")
		address = input("输入公司地址")
		card["name"]=name
		card["job"]=job
		card["phone"]=phone
		card["company"]=company
		card["address"]=address
		cards.append(card)
		print("新增成功")
	elif function == 2:
		print("查找名片")
		name = input("输入要查找的名字")
		for k in cards:
			if name == k["name"]:
				print(k)
			else:
				print("查找对象不存在")
	elif function == 3:
		print("修改名片")
		name = input("输入要查找的名字")
		for l in cards:
			if name == l["name"]:
				print(l)
				xuan = int(input("输入要修改的选项: 1.name 2.job 3.phone 4.company 5.address"))
				if xuan == 1:
					n_name = input("输入要修改的name:")
					l["name"]=n_name
					print(l)
				elif xuan == 2:
					job = input("输入要修改的job")
					l["job"]=job
					print(l)
				elif xuan == 3:
					phone = input("输入要修改的phone")
					l["phone"]=phone
					print(l)
				elif xuan == 4:
					company = input("输入要修改的company")
					l["company"]=company
					print(l)
				elif xuan == 5:
					address = input("输入要修改的address")
					l["address"]=address
					print(l)
				print(l)
	elif function == 4:
		print("删除")
		name = input("输入要删除的name")
		for d in cards:
			if name == d["name"]:
				print(d)
				cards.remove(d)
				print(cards)
