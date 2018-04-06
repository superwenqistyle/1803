'''
for i in range(1,4):
        account = input("请输入帐号")
        passwd = input("请输入密码")
        if account != "123456" or passwd != "123456":
            print("error%d次"%i)
        else:
            t = int(input("选择英雄范围: 0.ADC 1.肉 2.法师"))
            if t == 0:
                print("鲁班大师")
            elif t == 1:
                print("程咬金")
            elif t == 2:
                print("王昭君")
            break
'''
i = 1
while i <= 3:
	account = input("请输入帐号")
	passwd = input("请输入密码")
	if account != "123456" or passwd != "123456":
		print("error%d次"%i)
	else:
		t = int(input("选择英雄范围: 0.ADC 1.肉 2.法师"))
		if t == 0:
			print("鲁班大师")
		elif t == 1:
			print("程咬金")
		elif t == 2:
			print("王昭君")
		break
	i+=1
