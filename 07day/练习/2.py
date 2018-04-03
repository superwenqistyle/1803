number = int(input("请输入年分"))
if (number%4 == 0) and (number%100 !=0):
    print("闰年")
elif number%400 == 0:
    print("闰年")
