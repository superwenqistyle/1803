id_card = {"name":"liangwenqi","age":26,"school":"北财"}
print(id_card)
id_card["height"]=175
print(id_card)
id_card["age"]=165
print(id_card)
id_card.setdefault("addr","北京")
print(id_card)

print(id_card.keys())
print(id_card.values())

id_card.pop("name")
print(id_card)
del id_card["addr"]
print(id_card)
id_card.popitem()
print(id_card)
id_card1 = {"weight":148,"marry":"单身狗"}
id_card.update(id_card1)
print(id_card)
