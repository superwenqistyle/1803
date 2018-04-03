i =0
s_sum = 0
d_sum = 0
while i < 100:
    if i%2 == 0:
        s_sum += i
    elif i%2 == 1:
        d_sum += i
    i += 1
c = d_sum - s_sum
print(c)
