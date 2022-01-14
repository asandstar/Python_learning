import pandas as pd
import numpy as np
from pandas import DataFrame, Series
# 根据“数据科学系”实验教学计划，完成下面分析
# 1 读文件，创建DataFrame对象
df = pd.read_excel('C:\\data\\DataScience.xls', 'Sheet1', index_col=None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.unicode.ambiguous_as_wide', True)  # 处理数据的列标题与数据无法对齐的情况
pd.set_option('display.unicode.east_asian_width', True)   # 无法对齐主要是因为列标题是中文
# print(df)

# 2 查基本内容和总数
print(df.shape)
print(df.index)
print(df.columns)

# 3查询实验教学计划中是否含有NaN数据，
# 将含有NaN数据的行导出为数据文件pre.csv
# 判断采用何种数据清洗模式：填充、删除、手工填充
# 数据清洗模式：删除空行，删除重复行，删除数据缺失行
df.dropna(how='all', inplace=True)
# print(df)
# print(df.shape)
df.drop_duplicates(inplace=True)
# print(df)
# print(df.shape)

mask_3 = (df.isnull().values)
# print(mask_3)
df_NaN = df[mask_3]
# print(df_NaN)
df_NaN.to_csv('pre.csv')

df.dropna(inplace=True)
# print(df)
# print(df.shape)

# 4 查询'课程名称', '实验项目名称', '实验类型', '二级实验室名称'4列数据内容
print(df[['课程名称', '实验项目名称', '实验类型', '二级实验室名称']])

# 5 统计每门课程的实验课时数
group_5 = df.groupby(by='课程名称')
print(group_5.aggregate({'实验课时数': np.sum}))

# 6 统计每周开设的各门实验课的时数
group_6 = df.groupby(by='周次')
print(group_5.aggregate({'实验课时数': np.sum}))

# 7 统计每门课程的实验类型分布（crosstab）
print(pd.crosstab(df['课程名称'], df['实验类型']))

# 8 统计每个班级的实验课课表
class_8 = df['班级'].copy()
class_8.drop_duplicates(inplace=True)
class_8 = list(class_8)
# print(class_8)

for i in class_8:
    print(i+" 实验课课表")
    mask_8 = df['班级'].values == i
    # print(mask_8)
    table = df[mask_8]
    table.sort_values(by=['周次', '星期', '节次'], ascending=False)
    print(table)

# 9 分析各二级实验室承担的实验课时量
group_9 = df.groupby(by='二级实验室名称')
print(group_9.aggregate({'实验课时数': np.sum}))

# 10 分析各二级实验室可以支持的实验类型
print(pd.crosstab(df['二级实验室名称'], df['实验类型']))
