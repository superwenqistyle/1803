for i in range(2,101):
    count = 0
    for h in range(1,i+1):
    	if i%h == 0:
            count += 1
    if count == 2:
        print(i)

	    
