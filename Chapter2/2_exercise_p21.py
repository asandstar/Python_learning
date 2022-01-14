#1.一维数组访问
import numpy as np
names=np.array(['王微','肖良英','方绮雯','刘旭阳','钱易铭'])
subjects=np.array(['Math','English','Python','Chinese','Art','Database','Physics'])
scores=np.array([[70,85,77,90,82,84,89],
                 [60,64,80,75,80,92,90],
                 [90,93,88,87,86,90,91],
                 [80,82,91,88,83,86,80],
                 [88,72,78,90,91,73,80]])
#1）subject数组中选择并显示序号1、2、4门课的名称，使用倒序索引选择并显示names数组中“方绮雯”
print(subjects[[1,2,4]])
print(names[1:5])
#2）选择并显示names数组从2到最后的数组元素；选择并显示subjects数组正序2~4的数组元素
print(subjects[2:5])
#3）使用布尔条件选择并显示subjects数组中英语和物理科目名称
mask=(subjects=='English')|(subjects=='Physics')
print(subjects[mask])

#2.二维数组访问
#1）选取序号为1和4的行
print(scores[[1,4]])
#2）选取第1行和第4行的数学和python成绩
print(scores[[0,3]])
#3）选取所有学生的数学和艺术课成绩
print(scores[2:5:2,[0,2]])
#4）选取“王微”和“刘旭阳”的英语和艺术课成绩
print(scores[:,[0,4]])

#3.生成由整数10~19组成的2*5的二维数组
print(np.arange(10,20).reshape(2,5))
