a_ccount = "liangwenqi" 
p_asswd = 123456
i = 0
while True:
    account = input("请输入帐号")
    passwd = int(input("请输入密码"))
    if (account == a_ccount) and (passwd == p_asswd):
        hero = int(input("请输入要选择的英雄范围:1.ADC 2.肉 3.法师"))
        if hero == 1:
            print("鲁班大师")
        elif hero == 2:
            print("程咬金")
        elif hero == 3:
            print("王昭君")
        break
    else:
        i += 1
        print("error%d次"%i)
        if  i == 3:
            print("帐号被封")     		
            break 


        

