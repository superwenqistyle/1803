cards=[]
allsum=0
def print_menu():
	print("地铁费用计算程序".center(30,"*"))
	print("菜单列表".center(30," "))
	print("1.计算费用".center(30," "))
	print("2.记录打印".center(30," "))
	print("3.退出系统".center(30," "))
def function():
	while True:
		print_menu()
		number = int(input("请选择功能选项"))
		if number == 1:
			test()
		elif number == 2:
			print_card()
		else:
			break	

def test():
	card={}
	length,month,count = input_data()
	s_um = 0  #单次费用
	if length <= 6:
		money=3
	elif length > 6 and length <= 12:
		money=4
	elif length > 12 and length <= 22:
		money=5
	elif length > 22 and length <= 32:
		money=6
	else:
		if (length-32)%20 == 0:
			money = (length-32)%20 + 6
		else:
			money = int((length-32)%20) + 7
	
	for temp in range(30*count):
		if s_um > 100 and s_um <= 150:
			s_um+=0.8*money
		elif s_um >150 and s_um <= 400:
			s_um+=0.5*money
		s_um+=money
	print("************")
	global allsum
	allsum+=s_um
	card["month"]=month
	card["length"]=length
	card["s_um"]=s_um
	card["count"]=count
	card["allsum"]=allsum
	cards.append(card)
def input_data():
	l_ength = float(input("输入距离"))
	m_onth = int(input("输入月份"))
	c_ount = int(input("输入每天乘车次数"))
	if m_onth >= 1 and m_onth <= 12 and c_ount > 0:
		return l_ength,m_onth,c_ount
	else:
		print("输入格式不对")
def print_card():
	for temp in cards:
		print("月份:%d距离:%.02f次数:%d花费:%.02f总花费:%.02f"%(temp["month"],temp["length"],temp["count"],temp["s_um"],temp["allsum"]))
function()

