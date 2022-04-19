'''创建文件1-6.py，程序功能为：
（1）创建一个空列表
（2）在列表中，加入5位学生的姓名。
（提示，使用for循环和range()函数，每次循环输入1个学生的姓名，并将其加入到列表中）
（3）遍历列表，依次输出每个学生的姓名。
（4）输入一个学生的名字，检索是否已保存在列表中，找到输出yes ，否则输出 no。
（提示：列表有个操作，可以判断某个对象是否在列表中。
如：  5   in  [1,2,3,4,5]  得到的值为True）'''
a=[]
for i in range(5):
    x=input('Input a name:')
    a.append(x)
x=input('Find name:')
if x in a:
    print('Yes')
else:
    print('No')
