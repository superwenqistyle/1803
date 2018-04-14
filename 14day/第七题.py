def xxx():
	list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
	for temp in list:
		for k,v in temp.items():
			for p,j in v.items():
				print(k,p,j)	
xxx()
						
