list=[]
def hero(name):
	list.append(name)
while True:
	name = input("输入英雄")
	hero(name)

	if len(list) == 5:
		print(list)
		break
	
