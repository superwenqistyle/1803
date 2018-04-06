sum = 0 
m = 0
c = 1
for i in range(1,13):
   if i ==1 or i == 12:
       d = 32/31/2 #距离
   elif i == 2:
       d = 18/28/2
   elif i == 3 or i == 10:
       d = 7/31/2
   elif i == 4 or i == 9:
       d = 80/30/2
   elif i == 5 or i == 8:
       d = 34/31/2
   elif i == 6:
       d = 70/30/2 
   elif i == 7:
       d = 70/31/2
   elif d == 11:
       d = 18/30/2

   if d <= 6:
       m = 3 #路费
   elif d > 6 and d <= 12:
       m = 4
   elif d < 12 and d >= 22:
       m = 5
   elif d > 22 and d <= 32:
       m = 6
   elif d > 32:
       m = int((d - 32)/20) + 6 + 1
   if sum > 100 and sum <= 150:
       m = m*0.8
   elif sum >150 and sum <= 400:
       m= m*0.5
   if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==10 or i ==12:
       m = m*2*31
   elif i == 2:
       m = m*2*28
   else:
       m = m*2*30    
   sum = sum + m
   print("第%d月花费%d元"%(c,m))
   c += 1
print(sum)

