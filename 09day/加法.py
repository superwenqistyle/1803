x = int(input("请输入数字"))
y = int(input("请输入数字"))
s_um = 0
if x <= y:
    while x <= y:
        s_um = s_um + x
        x += 1
else:
    while y <= x:
        s_um = s_um + y
        y += 1

