'''
for i in range(9,0,-1):
	for j in range(1,i+1):
		print("%d*%d=%d\t"%(i,j,i*j),end = "")
	print("")
'''
'''
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print("%d*%d=%d\t"%(i,j,i*j),end = "")
		j+=1
	print("")
	i+=1
'''

i = 9
while i >=1:
	j = 1
	while j <= i:
		print("%d*%d=%d\t"%(j,i,i*j),end = "")
		j+=1
	print("")
	i-=1

