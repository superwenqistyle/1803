'''
c = 0
k = 0
for i in range(1,5001):
	k +=1
	if i%5 == 0 and i%7 == 0:
		c +=1
		print("第%d次输入\t第%d次输出%d"%(k,c,i))
'''
i = 0
k = 0
while i <= 5000:
	i+=1
	if i%5 == 0 and i%7 == 0:
		k+=1
		print("第%d次循环第%d次输出%d"%(i,k,i))



