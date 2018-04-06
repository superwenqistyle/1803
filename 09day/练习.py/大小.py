import random
h = random.randint(1,100)
c = 1
while c < 11:
    a = int(input("请输入数字:1~100之间"))
    b = int(input("判断结果:1.大 2.小"))
    if (h < a and b == 1) or (h > a and b == 2):
        print("猜测正确")
        break
    else:
        print("error%d"%c)
    c += 1
        
    
