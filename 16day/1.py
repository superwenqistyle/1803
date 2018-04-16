list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积”:"600平","人口":"150w"}}]:
for temp in list:
	for i,v in temp.items():
		for k,v in v.items():
			print(i,k,v)
