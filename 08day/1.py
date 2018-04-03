a_ccount = "liangwenqi"
p_asswd = 123456
account = input("请输入你的帐号")
passwd = int(input("请输入你的密码"))
i = 1
while (account != a_ccount) or (passwd != p_asswd):
    i += 1
    account = input("请输入你的帐号")
    passwd = int(input("请输入你的密码"))
    if i == 3: 
        print("帐号被封")
        break
if (account == a_ccount) and (passwd == p_asswd):
    hero = int(input("请选着你的英雄范围:0代表ADC 1代表肉 2代表法师"))
    if hero == 0:
        print("鲁班大师")
    elif hero == 1:
        print("陈咬紧")
    elif hero == 2:
        print("王昭君")    



        
