distance = 77
sum = 0
count = 1
while count <= 60:
    if distance <= 6:
    	money = 3
    elif distance > 6 and distance <= 12:
    	money = 4
    elif distance > 12 and distance <= 22:
    	money = 5
    elif distance >22 and distance <= 32:
    	money = 6
    elif distance >32:
    	money = int((distance - 32)/20) + 7
    if sum > 100 and sum <= 150:
    	money = money * 0.8
    elif sum > 150 and sum <= 400:
    	money = money * 0.5
    sum = sum + money
    count += 1
print("%.02f"%sum)   
