'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d\t"%(i,j,i*j),end = "")
        j+=1
    print("")
    i+=1
'''

for i in range(1,10):
    for h in range(1,i+1):
        print("%d*%d=%d\t"%(i,h,i*h),end = "")
    print("")
