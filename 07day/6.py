height = float(input("请输入身高"))
shenjia = float(input("请输入身价"))
yanzhi = float(input("请输入颜值"))
if height > 180 and shenjia > 1000000 and yanzhi > 90:
    print("高富帅哥")
elif height < 180 and shenjia > 1000000 and yanzhi > 90:
    print("富帅")
elif height < 180 and shenjia < 1000000 and yanzhi >90:
    print("帅")
elif height < 160 and shenjia < 100 and yanzhi <60:
    print("矮戳穷")     
