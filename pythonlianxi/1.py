name = input("请输入名字:")
print("我的名字叫%s，请多多关照!"%name)

student_no = input("请输入学号")
print("我的学号是%s"%student_no)

price = float(input("请输入西瓜单价"))
weight = float(input("请输入西瓜重量"))
money = price*weight
print("西瓜单价%f\n购买了%f\n需要支付%f"%(price,weight,money))

scale = float(input("请输入小数"))
print("数据比例是%02f%%"%(scale*100))
