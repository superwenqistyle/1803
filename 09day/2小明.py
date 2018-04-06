sum = 0  #每月的钱数
s_sum = 0  #每次的钱数
#mon = 0  每一月总钱
m = 0  #每一次坐车钱
for i in range(1,13):
    if i == 1 or i == 12:
        d = 32  #距离
    elif i == 2:
        d =18
    elif i == 3 or i == 10:
        d = 7
    elif i == 4 or i == 9:
        d = 80
    elif i == 5 or i == 8:
        d = 34
    elif i == 6:
        d = 70
    elif i == 7:
        d = 70
    elif i == 11:
        d = 18
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        p = 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        p = 30
    else:
        p = 28
    for k in range(1,2*30+1):
        if d <= 6:
            m = 3  #每次的路费
        elif d > 6 and d <= 12:
            m = 4
        elif d > 12 and d <= 22:
            m = 5
        elif d > 22 and d <= 32:
            m = 6
        elif d > 32:
            if (d-32)/20 == 0:
                m = (d-32)/20 == 0
            else:
                m = int((d - 32)/20) + 6 + 1

        if s_sum > 100 and s_sum <= 150:
            m = m*0.8
        elif s_sum > 150 and s_sum <= 400:
            m = m*0.5
        s_sum = s_sum + m
    print("第%d月花费%d元"%(i,s_sum))
#    sum = sum + s_sum
#print(sum)
