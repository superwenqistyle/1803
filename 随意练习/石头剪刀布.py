import random
c = random.randint(1,3)
for i in range(1,21):
	h = int(input("输入你的选择: 1.石头 2.剪刀 3.布"))
	if (i ==1 and c == 2) or (i == 2 and c == 3) or (i == 3 and c == 1):
		print("wow!电脑弱爆了")
		# break
	elif i == c:
		print("SM情况")
	else:
		print("电脑要超神!??")
print("game over")
