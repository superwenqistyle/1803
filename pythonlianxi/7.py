price = float(input("输入商品的价格"))
weight = float(input("输入商品的重量"))
ys_money = price*weight
money = float(input("实际面付金额"))
s_money = money - ys_money
print(s_money)

