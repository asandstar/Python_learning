import pandas as pd
import numpy as np
from pandas import DataFrame
print("1.数据合并")
print("1)从xlsx的group3中读数据，将'序号', '性别', '年龄'保存到data1")
data = pd.read_excel('C:\\data\\studentsInfo.xlsx', 'Group3')
pd.set_option('display.unicode.ambiguous_as_wide', True)  # 处理数据的列标题与数据无法对齐的情况
pd.set_option('display.unicode.east_asian_width', True)   # 无法对齐主要是因为列标题是中文
Info1 = ['序号', '性别', '年龄']
data1 = DataFrame(data, columns=Info1)
# data1.index=data1.index.droplevel('序号')#
print(data1)

print("2)从xlsx的group3中读数据，将'序号', '身高', '体重', '成绩'保存到data2")
Info2 = ['序号', '身高', '体重', '成绩']
data2 = DataFrame(data, columns=Info2)
# data2.index=data2.index.droplevel('序号')#
print(data2)
print("3)data2合并到data1，内连接")
data3 = pd.merge(data1, data2, how='inner', left_on='序号', right_on='序号')
print(data3)
'''这里merge总是出现问题
用上index_col=0则'序号' is both an index level
and a column label, which is ambiguous.
不用则第一列总是有0，1，2……9
太让我伤心了'''
