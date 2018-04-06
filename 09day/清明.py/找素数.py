'''
for i in range(2,101):
	c = 0
	for h in range(1,i+1):
		if i%h == 0:
			c+=1
	if c == 2:
		print(i)
'''


i = 2
while i <= 100:
    h = 1
    c = 0
    while h <= i:
        if i%h == 0:
            c+=1
        h+=1
    if c == 2:
        print(i)
    i+=1
