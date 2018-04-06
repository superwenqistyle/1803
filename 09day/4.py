sum = 0
for i in range(1,13):
    if i ==1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        m = 31  #天数
    elif i == 4 or i == 6 or i == 9 or i == 11:
        m = 30
    else:
        m = 28 
    if i == 1 or i == 12:
        d = 32  #距离
    elif i == 2 or i == 11:
        d = 18
    elif i == 3 or i == 10:
        d = 7
    elif i == 4 or i == 9:
        d = 80
    elif i ==5 or i == 8:
        d == 34
    else:
        d == 70
    s_um = 0
    for k in range(1,2*m+1):
        if d <= 6:
            mon = 3
        elif d > 6 and d <= 12:
            mon = 4
        elif d > 12 and d <= 22:
            mon = 5
        elif d > 22 and d <=32:
            mon =6
        elif d > 32:
            if (d-32)%20 == 0:
                mon = (d-32)/20 + 6
            else:
                mon = int((d-32)/20) + 7
        if s_um > 100 and s_um <= 150:
            s_um = s_um + float(0.8*mon)
        elif s_um > 150 and s_um <= 400:
            s_um = s_um + float(0.5*mon)
        else:
            s_um = s_um + mon
    print("第%d月花费%.02f元"%(i,s_um)) 
    sum = sum + s_um
print(sum)
     
