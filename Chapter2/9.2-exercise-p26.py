import numpy as np
names=np.array(['王微','肖良英','方绮雯','刘旭阳','钱易铭'])
subjects=np.array(['Math','English','Python','Chinese','Art','Database','Physics'])
scores=np.array([[70,85,77,90,82,84,89],
                 [60,64,80,75,80,92,90],
                 [90,93,88,87,86,90,91],
                 [80,82,91,88,83,86,80],
                 [88,72,78,90,91,73,80]])
#1.所有学生的英语成绩减3分并显示
print(scores[:,[1]]-3)
#2.统计每名学生所有科目的平均分并显示
print(scores.mean(axis=1))
#3.用随机函数生成[-1,1]之间服从均匀分布的3*4二维数组
#计算所有元素的和
print(np.random.uniform(-1,2,size=(3,4)))
print(np.random.uniform(-1,2,size=(3,4)).sum())
