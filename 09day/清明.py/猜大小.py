'''
import random
c = random.randint(1,100)
for i in range(1,11):
	t = int(input("请输入1~100之间的数:"))
	if t > c:
		print("猜大了")
	elif t < c:
		print("猜小了")
	else:
		if i < 3:
			print("you are superman")
		print("猜中了")
		break
'''

import random
c = random.randint(1,100)
i = 0
while i < 10:
	i+=1
	t = int(input("请输入1~100数字"))
	if t > c:
		print("猜大了")
	elif t < c:
		print("猜小了")
	else:
		print("猜中了")
		break
