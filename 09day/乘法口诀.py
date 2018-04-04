i = 1
while i <= 9:
    print("%d."%i,end = "")
    j = 1
    while j <= i:
         m = i * j
         print("%d*%d=%d "%(i,j,m),end = "")
         j += 1
    print("")
    i += 1

