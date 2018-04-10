print("商品交易系统v1.0版本".center(90,"*"))
print("系统功能: 1.商品价格录入 2.查看商品价格 3.修改商品价格 4.删除商品价格 5.商品交易 6.查看交易记录 7.退出系统".center(20,"*"))
coms=[]  #商品列表
while True:
	function = int(input("请选择功能项: 1.商品价格录入 2.查看商品价格 3.修改商品价格 4.删除商品价格 5.商品交易 6.查看交易记录 7.退出系统"))
	if function == 1:
		com={}  #单个商品的信息
		print("价格录入")
		flag = 0  #默认flag=0表示不在商品库
		name = input("请输入商品名")
		for temp in coms:
			if name in temp["name"]:
				flag = 1
				break
		if flag == 1:
			print("商品名字重复,请重新输入")
			continue
		price = float(input("请输入商品价格"))
		com={"name":name,"price":price}
		coms.append(com)
		print("新增商品成功")
		print(coms)
	elif function == 2:
		print("查找商品")
		name = input("输入要查找的商品")
		for temp in coms:
			if name == temp["name"]:
				print(temp)
			else:
				print("请重新输入商品名称")
	elif function == 3:
		print("修改商品")
		name = input("输入要修改的商品")
		for temp in coms:
			if name == temp["name"]:
				print(temp)
				t = int(input("请输入要修改的选项: 1.商品名称 2.价格"))
				if t == 1:
					n_ame = input("输入要修改后的的商品的名称")
					temp["name"]=n_ame		
					print(temp)
				elif t == 2:
					p_rice = float(input("请输入价格"))
					temp["price"]=p_rice
					print(temp)
	elif function == 4:
		print("删除商品")
		name = input("输入要删除的商品")
		for temp in coms:
			if name == temp["name"]:
				print(temp)
				coms.remove(temp)
				print(coms)
	elif function == 5:
		print("商品交易")
		sum = 0
		p_rice = float(input("输入收款金额额"))
		zhonglei = int(input("请输入商品种类数目"))
		for k in coms:
			name = input("输入商品种类")
			for temp in coms:
				if name == temp["name"]:
					cishu = int(input("输入件数"))
					t = temp["price"]*cishu
					sum+=t
					break
		print("本次消费%.02f元,找零%.02f元"%(sum,p_rice-sum))
	elif function == 6:
		print("查看交易记录")
	elif function:
		break	
