from random import randint
import time
cards=[]
def print_menu():
	print("员工管理系统".center(30,"*"))
	print("1.员工入职".center(30,"*"))
	print("2.查看记录".center(30,"*"))
	print("3.员工离职".center(30,"*"))
	print("4.退出系统".center(30,"*"))
def input_function():
	while True:
		print_menu
		fun = int(input("选择功能"))
		if fun == 1:
			addUser()
		elif fun == 2:
			findUser()
		elif fun == 3:
			outCompany()
		else:
			break
def addUser():
	name = input("请输入姓名")
	worknumber = int(input("请输入工号"))
	age = int(input("请输入年龄"))
	job = input("请输入工作")
	salary = float(input("请输入薪酬"))
	creat_time = input("输入一个时间")
	dict["name"]=name
	dict["worknumber"]=worknumber
	dict["age"]=age
	dict["job"]=job
	dict["salary"]=salary
	dict["creat_time"]=creat_time
	list.append(dict)
def findUser():
	name = input("输入姓名")
	for temp in cards:
		if name == temp["name"]:
			print("姓名:%s"%name)
			print("工号:%d"%temp["worknumber"])
			print("年龄:%d"%temp["age"])
			print("工作岗位:%s"%temp["job"])
			print("每月薪酬:%.02f"%temp["salary"])
			print("入职")
	pass
def outCompany():
	pass
		
