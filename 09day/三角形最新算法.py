i = int(input("请输入数字"))
l = 1
while l <= i:
    print(" "*(i-l),end = "")
    j = 1 
    while j <= l:
        print("* ",end = "")
        j += 1
    print("")
    l += 1

