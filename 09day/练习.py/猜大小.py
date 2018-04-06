import random
h = random.randint(1,100)
y= 1
while True:
    i = int(input("请输入数字"))
    k = int(input("输入猜测结果: 1.大 2.小"))
    if h < i and k == 1:
        print("猜对了")
    elif i < h and k== 2:
	break
    else:
	print("error%d次"%y)
	y = y + 1
	if y > 10:
	    print("game over")
            break
