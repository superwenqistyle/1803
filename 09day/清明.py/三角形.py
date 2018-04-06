'''
k = int(input("输入行数"))
for i in range(k,0,-1):
	print(" "*i,end = "")
	for j in range(1,k+2-i):
		print("* ",end = "")
	print("")
'''
n = int(input("输入行数"))
k = 1
while k <= n:
	print(" "*(n-k),end = "")
	i = 1
	while i <= k:
		print("* ",end = "")
		i+=1
	print("")
	k+=1
