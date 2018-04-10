'''
list = [1,2,3,4,5,6,7]
for i in list:
	list.remove(i)
print(list)
'''
'''
list = [1,2,3,4,5,6,7]
for i in range(len(list)):
	list.pop(i)
'''
'''
list = [1,2,3,4,5,6,7]
for i in range(len(list)-1,-1,-1):
	list.pop(i)
	print(list)
'''

list = [1,2,3,4,5,6,7]

new_list = list[:]
for i in new_list:
	list.remove(i)


	print(list)
