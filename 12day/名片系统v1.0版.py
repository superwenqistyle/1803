print("名片系统".center(60,"*"))
print("1.新增名片".center(60,"*"))
print("2.查找名片".center(60,"*"))
print("3.修改名片".center(60,"*"))
print("4.删除名片".center(60,"*"))
print("5.遍历名片".center(60,"*"))
print("6.退出系统".center(60,"*"))
cards=[]
order=0
import time
while True:
	function = int(input("请选择功能选项: 1.新增 2.查找 3.修改 4.删除 5.遍历名片 6.退出系统"))
	if function == 1:
		print("新增名片".center(60,"*"))
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
		isdelete = 1  #默认为存在
		order+=1
		time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
		job = input("输入工作")
		phone = int(input("输入电话号码"))
		company = input("输入公司")
		address = input("输入公司地址")
		card["isdelete"]=isdelete
		card["time"]=time
		card["order"]=order
		card["name"]=name
		card["job"]=job
		card["phone"]=phone
		card["company"]=company
		card["address"]=address
		cards.append(card)
		print("新增成功")
	elif function == 2:
		print("查找名片".center(60,"*"))
		name = input("输入要查找的名字")
		flag = 0
		for k in cards:
			if name == k["name"] and k["isdelete"] == 1:
				print("序号:%d\t姓名:%s\t工作:%s\t电话号码:%d\t公司:%s\t公司地址:%s\t最后更新时间:%s"%(k["order"],k["name"],k["job"],k["phone"],k["company"],k["address"],k["time"]))
				flag = 1
				break
		if flag == 0:
			print("查找对象不存在")
	elif function == 3:
		print("修改名片".center(60,"*"))
		name = input("输入要查找的名字")
		flag = 0 #默认不存在
		for l in cards:
			if name == l["name"] and l["isdelete"]:
				print("序号%d\t姓名:%s\t工作:%s\t电话号码:%d\t公司:%s\t公司地址:%s\t最后更新时间:%s"%(l["order"],l["name"],l["job"],l["phone"],l["company"],l["address"],l["time"]))
				flag = 1
				xuan = int(input("输入要修改的选项: 1.name 2.job 3.phone 4.company 5.address"))
				if xuan == 1:
					n_name = input("输入要修改的name:")
					l["name"]=n_name
				elif xuan == 2:
					job = input("输入要修改的job")
					l["job"]=job
				elif xuan == 3:
					phone = input("输入要修改的phone")
					l["phone"]=phone
				elif xuan == 4:
					company = input("输入要修改的company")
					l["company"]=company
				elif xuan == 5:
					address = input("输入要修改的address")
					l["address"]=address
				else:
					print("输入不合理,请重新输入")
					continue
				time = time.strftime("%Y-%m-%d %H:%M:%S")
				l["time"]=time
		if flag == 0:
			print("名字不存在")
	elif function == 4:
		print("删除名片".center(60,"*"))
		name = input("输入要删除的name")
		flag = 0  #默认不存在
		for d in cards:
			if name == d["name"] and d["isdelete"] == 1:
				flag = 1
				sure = int(input("0.确认删除 1.取消返回"))
				if sure == 0:
					d["isdelete"]=0
					#cards.remove(d)
					#print(cards)
				break
		if flag == 0:
			print("名字不存在")
	elif function == 5:
		print("遍历名片".center(60,"*"))
		for temp in cards:
			if temp["isdelete"] == 1:
				print("序号%d\t姓名:%s\t工作:%s\t电话号码:%d\t公司:%s\t公司地址:%s\t最后更新时间:%s"%(temp["order"],temp["name"],temp["job"],temp["phone"],temp["company"],temp["address"],temp["time"]))
	elif function == 6:
		print("退出名片系统".center(60,"*"))
		sure = int(input("选项: 0.确认删除 1.取消返回"))
		if sure == 0:
			break
		elif sure == 1:
			continue

	else:
		print("输入有误".center(60,"*"))
