list=[]
def k():
	d = input("输入一个输出的英雄")
	list.append(d)

while True:
	k()
	if len(list) == 5:
		print(list)
		break
