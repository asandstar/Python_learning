#1. 输入教材P10—11中的语句，熟悉常用数据类型。
#注意：字符串，元组，列表是序列数据，有索引。
#字典中的元素是‘键--值’对，字典中的元素是无序的，通过‘键’可以找到与之关联的‘值’。
s=input("姓名和年龄：")
name,age=s.split(",")
print(name,age)
print("name:{},age:{}".format(name,age))
