import random
a = random.randint(1,100)
i = 0
while True:
    b = int(input("请输入一个数字"))
    c = int(input("请输入猜测结果:1.大 2.小"))  #大:输入>系统
    if b > a and c == 1:
        break
    elif b < a and c == 2:
        break
    else:
        i += 1
        print("error%d次"%i)
        if i == 10:
            print("game over")
        
