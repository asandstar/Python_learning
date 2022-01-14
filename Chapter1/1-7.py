'''创建文件1-7.py，程序功能为：
（1）使用字典，记录5位学生的姓名和身高。
dic={‘zhang’:180,  ’wang’:160,  ‘Li’:175,  ‘zhao’: 170, ‘ding’:165}
（2）遍历字典，输出每个学生的姓名和身高。（提示：for循环）
（3）输入其中任意一个学生的姓名，查找并显示所有高于此身高值的学生信息。（如输入 zhao，则输出zhang,Li两位学生的名字和身高）。'''
d={'zhang':180,'wang':160,'Li':175,'zhao': 170, 'ding':165}
for name in d:
    print("name:{:s},height:{:d}".format(name,d[name]))
nm=input('input a student name:')
if nm not in d:
    print('name not exist')
else:
    print('higher:')
    hi=d[nm]
    for name in d:
        if d[name]>hi:
            print('{:s}:{:d}'.format(name,d[name]))
