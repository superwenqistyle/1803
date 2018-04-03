ccout = input("请输入账号")
passwd = input("请输入密码")
if (accout == "123456") and (passwd == "abc"):
    print("登录成功")
elif (accout != "123456") and (passwd == "abc"):
    print("账号不对")
elif (accout == "123456") and (passwd != "abc"):
    print("密码不对")
