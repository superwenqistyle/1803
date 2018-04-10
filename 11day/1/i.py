list=[["传奇","贪玩蓝月"],["qq飞车","qq炫舞"],["天天酷跑","天天炫斗"],["王者荣耀","绝地求生"]]
t = int(input("输入第一个索引"))
y = int(input("输入第二个索引"))
for i in range(0,len(list)):
	if i == t-1:
		list1=list[i]
		print(list1[y-1])
