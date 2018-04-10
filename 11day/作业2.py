list=[]
list_name=[]
dict={}
dict_name={}
i=1
while True:
	name = input("输入名字")
	age = int(input("输入年龄"))
	sex = input("输入性别")
	qq = int(input("输入qq"))
	weight = int(input("输入体重"))
	dict_name={"name":name}  # "age":age,"sex":sex,"qq":qq,"weight":weight}
#	print(dict_name)
	list_name.extend(dict_name)
#	print(list_name)
#	for k in range(0,i):
#		print(i)
	if name not in list_name:
		dict={"name":name,"age":age,"sex":sex,"qq":qq,"weight":weight}
		list.append(dict)
		i+=1
	else:
		print("名字重复,再输一次")
	if i > 3:
		break
print(list)
				
