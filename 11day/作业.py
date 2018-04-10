list=[]
list_name=[]
dict={}
list_name={}
i=1
while True:
	name = input("输入名字")
	age = int(input("输入年龄"))
	sex = input("请输入性别")
	QQ = int(input("请输入qq号"))
	weight = int(input("请输入体重"))
'''
	if i == 1:
		dict={"name":name,"age":age,"sex":sex,"QQ":QQ,"weight":weight}

		list.append(dict)
'''
'''
	for a in list:
		#print(a)
		for k in a.get("name"):
'''			
	list_name = {"name":name}
	list_name.extend(list_name)
	for k in list_name:
		if i > 1 and name == k:
			print("名字重复,请重新输入")
			break
		else:
			dict={"name":name,"age":age,"sex":sex,"QQ":QQ,"weight":weight}
			list.append(dict)
			i+=1
	if i > 4:
		break
print(list)
