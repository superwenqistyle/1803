'''
import random
c = random.randint(1,100)
for i in range(1,11):
    h = int(input("请输入数字"))
    if c < h:
        print("猜大了")
    elif c > h:
        print("猜小了")
    else:
        print("猜对了")
'''
import random
c = random.randint(1,100)
i = 1
while i <11:
    h = int(input("请输入数字"))
    if c < h:
        print("猜大了")
    elif c > h:
        print("猜小了")
    else:
        print("猜对了")
    i += 1  
