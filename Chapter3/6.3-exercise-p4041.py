# 1.创建并访问series对象
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# 1）创建series对象，a~f是索引标签
m = Series([30, 25, 27, 41, 25, 34], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(m)
# 2）增加数据27，索引为g
s = Series([27], index=['g'])
n = m.append(s)
print(n)
# 3）修改索引d对应的值为40
n['d'] = 40
print(n['d'])
# 4）查询大于27的数据
print(n[n.values > 27])
# 5）删除位置为1~3的数据  这里我做的不太好
p = m.drop(['b', 'c', 'd'])
print(p)
# 2.创建并访问DataFrame对象
# 1）创建DataFrame数据对象，内容如下
data = [[3, 2, 1], [5, 4, 6], [9, 8, 7]]
num = DataFrame(data, index=['a', 'b', 'c'], columns=['one', 'two', 'three'])
print(num)
# 2）查询列索引为two,three的两列数据
print(num.loc[:, ['two', 'three']])
# 3）查询第0，2行和第0，2列数据
print(num.iloc[[0, 2], [0, 2]])
# 4）筛选第1列中值大于2的所有行数据，另存为data1对象
mask = num['one'] > num['two']
data1 = num.loc[mask, ['one', 'two', 'three']]
print(data1)
# 5）为data1添加一列数据，列索引为four，值都为10
data1['four'] = [10, 10, 10]
print(data1)
# 6）将data1所有值大于9的数据改为8
mask = data1['four'] > 9
data1.loc[mask, ['four']] = 8
print(data1)
# 7）删除data1中第0行和第1行数据
print(data1.drop(['a', 'b'], axis=0))
'''a little reminder
1）生成1~9的二维ndarray数据对象，使用NumPy的arange()和reshape()函数
2）使用data>9生成布尔型DataFrame，用于DataFrame所有值过滤
'''
