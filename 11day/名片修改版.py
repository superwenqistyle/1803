list=[]
list_name=[]
dict={}
i=1
while True:
		#print("重新输入ming")
		#continue
	#else:
	name = input("输入名字")
	if name not in list_name:
		age = int(input("输入年龄"))
		sex = input("请输入性别")
		QQ = int(input("请输入qq号"))
		weight = int(input("请输入体重"))
		dict={"name":name,"age":age,"sex":sex,"QQ":QQ,"weight":weight}
		list.append(dict)
		list_name.append(name)
		print(list)
		i+=1
	else:
		print("名字重复,再输入一次")
		continue
	if i == 4:
		break
sum_age = 0
for i in list:
	sum_age += i["age"]
print("平均年龄是%.02f"%((sum_age)/len(list)))
		#if i > 4:

	#if i == 1:
		#dict={"name":name,"age":age,"sex":sex,"QQ":QQ,"weight":weight}

		#list.append(dict)
	#for a in list:
		#print(a)
		#for k in a.get("name"):	
	#list_name = {"name":name}
	#list_name.extend(list_name)
	#for k in list_name:
		#if i > 1 and name == k:
			#print("名字重复,请重新输入")
			#break
		#else:
#		break
#print(list)
