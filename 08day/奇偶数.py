'''
i = 1
d_sum = 0
s_sum = 0
while i <=100:
    if i%2 == 0:
        d_sum = d_sum + i
    else:
        s_sum = s_sum + i  
    i += 1
print(d_sum) 
print(s_sum)   
'''

d_sum = 0
s_sum = 0
for i in range(1,101):
	if i%2 == 0:
		d_sum+=i
	else:
		s_sum+=i
print(d_sum)
print(s_sum)
