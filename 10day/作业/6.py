jucan=["wang","he","you"]
for i in jucan:
	print("邀请%s来聚餐"%i)
print("找到一个更大的餐桌")
jucan.insert(0,"kai")
jucan.insert(2,"shi")
jucan.append("wangzhe")
for j in jucan:
	print("向%s发出邀请"%j)
print("我只能邀请两个人")
jucan.pop()
print("'wangzhe'很抱歉,无法邀请你共进晚餐")
jucan.pop()
print("'you'很抱歉,无法邀请你共进晚餐")
jucan.pop()
print("'he'很抱歉,无法邀请你共进晚餐")
jucan.pop()
print("'wang'很抱歉,无法邀请你共进晚餐")
for i in jucan:
	print("%s仍在受邀之列"%i)
del jucan[0]
del jucan[0]
print(jucan)
print("邀请了%d位嘉宾"%len(jucan))


