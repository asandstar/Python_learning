import pandas as pd
import numpy as np
print("1.数据清洗")
print("1)读取数据")
stu = pd.read_excel('C://data//studentsInfo.xlsx', 'Group1', index_col=0)
pd.set_option('display.unicode.ambiguous_as_wide', True)  # 处理数据的列标题与数据无法对齐的情况
pd.set_option('display.unicode.east_asian_width', True)   # 无法对齐主要是因为列标题是中文
print(stu)
print("2）将“案例教学”列数据值全改为NaN")
stu['案例教学'] = np.nan
print(stu)
print("3)滤除每行数据中缺失》=3项的行")
stu1 = stu.dropna(thresh=7)
print(stu1)
print("4）滤除值全部为NaN的列")
stu2 = stu.dropna(axis=1, how='all')
print(stu2)

print("2.数据填充 继续用上面的数据")
print("2）用列平均值填充“体重”和“成绩”列的NaN数据（注意是mean不是avarage）")
stu3 = stu2.fillna({'体重': stu['体重'].mean(), '成绩': stu['成绩'].mean()})
print(stu3)
print("3）用上一行数据填充“年龄”列的NaN数据")
stu4 = stu3.fillna({'年龄': stu['年龄'].ffill()})
print(stu4)
print("4）用“中位数”填充“生活费用”列的NaN数据")
stu5 = stu4.fillna({'月生活费': stu['月生活费'].median()})
print(stu5)
