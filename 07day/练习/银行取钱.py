accout = "123456"
passwd = "123456"
money = 2000000
a_ccout = input("请输入账号")
p_asswd = input("请输入密码")
if (a_ccout == accout) and (p_asswd == passwd):
    q_money = float(input("请输入取钱金额"))
    s_money = 2000000 - q_money
    if s_money < 0:
        print("没钱取毛线")
    else:
        print("取了%f钱，还剩%f钱"%(q_money,s_money)) 
else:
    print("非法账户")
