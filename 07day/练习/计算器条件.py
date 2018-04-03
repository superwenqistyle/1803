x = float(input("请输入数字"))
y = float(input("请输入数字"))
tar = input("请输入运算符号:+-*/**")
if tar == "+":
    print(x+y)
else:
    if tar == "-":
        print(x-y)
    else:
        if tar == "*":
            print(x*y)
        else:
            if tar == "/":
                print(x/y)
            else: 
                if tar == "**":  
                    print(x**y)

