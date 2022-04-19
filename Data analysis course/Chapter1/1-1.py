#创建文件1-1.py，输入教材P12中3的语句段，并运行。熟悉python编程语言的输入和输出语句。
s=input("姓名和年龄：")
name,age=s.split(",")
print(name,age)
print("name:{},age:{}".format(name,age))
