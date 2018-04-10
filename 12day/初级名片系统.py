list=[]
list_name=[]
dict={}
i=1
while i <4:
	name = input("输入名字")
	if name in list_name:
		print("名字重复")
		continue
	#age = int(input("输入年龄"))
	#sex = input("输入性别")
	#QQ = int(input("输入qq号"))
	#weight = float(input("输入体重"))
	#if name in list_name:
		#print("名字重复")
		#continue
	else:
		age = int(input("输入年龄"))
		sex = input("输入性别")
		QQ = int(input("输入qq号"))
		weight = float(input("输入体重"))
		#dict["name"]=name
		#dict["age"]=age
		#dict["sex"]=sex
		#dict["QQ"]=QQ
		#dict["weight"]=weight
		dict={"name":name,"age":age,"sex":sex,"QQ":QQ,"weight":weight}
		list.append(dict)
		list_name.append(name)
		print(list)
		i+=1
sum_age = 0
for i in list:
	sum_age += i["age"]
print("平均年龄是%0.2f"%(sum_age/len(list)))
for j in list:
	name_title == input("输入要查找的人的姓名")
	if name_title == j["name"]:
		l_ist = int(input("输入要修改的选项: 1.name 2.age 3.sex 4.QQ 5.weight"))
		if l_ist == 1:
		n_ame = input("输入修改后的name")
		j["name"]=n_ame
		elif l_ist == 2:
		a_ge = input("输入修改后的age")
		j["age"]=a_ge
		elif l_ist == 2:
		s_ex = input("输入修改后的sex")
		j["s_ex"]=s_ex
		elif l_ist == 3:
		Q_Q = input("输入修改后的QQ")
		j["QQ"]=Q_Q
		elif l_ist == 3:
		w_eight = input("输入修改后的weight")
		j["weight"]=w_eight
		
	else:
		print("本地数据无此人,请重新输入")

