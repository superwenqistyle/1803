'''
sum = 0
for i in range(1,100):
	sum = sum + i*((-1)**(i+1))
print(sum)
'''

'''
sum = 0
i = 1
while i <= 99:
	sum = sum + i*((-1)**(i+1))
	i+=1
print(sum)
'''
'''
sum = 0
i = 1
while i <= 99:
	if i%2 == 0:
		sum = sum - i
	else:
		sum = sum + i
	i+=1
print(sum)
'''

s_h = 0
s_j = 0
i = 1
while i <= 99:
	if i%2 == 1:
		s_h+=i
	else:
		s_j+=i
	i+=1
print(s_h-s_j)

