accout = input("请输入你的帐号")
passward = input("请输入密码")
nich_name = input("请输入姓名")
money = 200000  #原有存款
need_money = input("请输入您要提取的金额")
s_um = money - int(need_money)
print("帐号%s\n密码******\n姓名%s\n原有金额%s\n取款金额%s\n剩余金额%s"%(accout,nich_name,money,need_money,s_um))
