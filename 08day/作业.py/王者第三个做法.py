account = "liangwenqi"
passwd = 123456
i = 1
a_ccount = input("请输入账户")
p_asswd = int(input("请输入密码"))
if (a_ccount == account) and (p_asswd == passwd):
    hero = int(input("请输入英雄的范围: 1.ADC 2.肉 3.法师"))
    if hero == 0:
        print("鲁班大师")
    elif hero == 1:
        print("程咬金")
    elif hero == 2:
        print("王昭君")
else:
    while True:
        print("error%d次"%i)
        a_ccount = input("请输入账户")
        p_asswd = int(input("请输入密码"))
        i += 1
        if i == 3:
            print("帐号被封")
            break 
                
