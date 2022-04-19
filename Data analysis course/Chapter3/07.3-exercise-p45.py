import pandas as pd
import numpy as np
from pandas import DataFrame
# 1.创建50*7的DataFrame对象，[10，99]之间随机整数
data = np.random.randint(10, 100, 350).reshape(50, 7)
# columns是字符a~g
num = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(num)
# df保存到csv
num.to_csv('out.csv', mode='w', header=True, index=False)

# 2.海伦在线交友
# 1）读取有效数据保存到DataFrame，跳过所有文字解释行
# 2）列索引名设为['flymiles', 'videogame', 'icecream', 'type']
data1 = pd.read_csv('C:data\\datingTestSet.csv', header=None, names=['flymiles', 'videogame', 'icecream', 'type'], skiprows=2, engine='python')
# 3）显示读取到的前5条数据
print(data1[:5])
# 4）显示所有'type'为'largeDoses‘的数据
mask = data1['type'] == 'largeDoses'
print(data1.loc[mask, :])
