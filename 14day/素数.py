def shu():
	for temp in range(100,201):
		k = 0
		for i in range(2,temp):
			if temp%i == 0:
				k+=1
		if k == 0:
			print(temp)
				#continue

			
shu()
