x = int(input("请输入数字"))
y = int(input("请输入数字"))
j = 1
sum = 0
if x < y:
    for i in range(x,y+1):
        sum = sum + i
        print(sum)
else:
    while True:
        print("输入错误%d"%j)
        x = int(input("请输入数字"))
        y = int(input("请输入数字"))
        j += 1
        if j == 3:
            break
