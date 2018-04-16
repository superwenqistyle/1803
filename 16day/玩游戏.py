import time
def play_game():
	for i in range(10):
		print("玩吃鸡 哒哒哒")
		time.sleep(1)
	print("你爸爸来")
	t = kill()
	if t == "削死了":
		print("game over")
	else:
		print("go on play game")



def kill():
	print("一顿次奥")
	say()
	return "削惨了惨了"
def say():
	print("打死你尕娃你个龟孙")
play_game()
