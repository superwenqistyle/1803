list=[{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]


for i in list:
	#print(i)
	#i是字典
	for l,j in i.items():
		#k = beijing
		#v = {"mianji":1290}
		#print(k)
		#print(v)
		for k,v in j.items():
			print(l,k,v)

