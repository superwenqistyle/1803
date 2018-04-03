import random
while True:
    computer = random.randint(1,3)
    play1 = int(input("请输入石头---1,剪刀---2,布---3"))
    if (computer==1 and play1==2) or (computer==2 and play1==3) or (computer==3 and play1==1):
        print("电脑赢")
    elif computer == play1:
        print("平局")
    else:
        print("玩家")
