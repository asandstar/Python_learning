print('思考与练习1')
# 1、数据读取
import pandas as pd
filename = 'c:/data/advertising.csv'
data = pd.read_csv(filename, index_col=0)
x = data.iloc[:, 0:3].values.astype(float)
y = data.iloc[:, 3].values.astype(float)

# 2、将自变量数组和目标变量数组划分为训练集（train）和测试集（test）
from sklearn import model_selection
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.35, random_state=1)

# 3、在全部数据上学习回归模型linregTr
from sklearn.linear_model import LinearRegression
linregTr = LinearRegression()
linregTr.fit(x, y)
print(linregTr.intercept_, linregTr.coef_)

# 4、在测试集上应用模型，计算预测结果，RMSE和决定系数R^2
from sklearn import metrics
y_train_pred = linregTr.predict(x_train)
y_test_pred = linregTr.predict(x_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred)
test_err = metrics.mean_squared_error(y_test, y_test_pred)
print('The man squar error of train and test are:{:.2f},{:.2f}'.format(train_err, test_err))

# 5、在测试集上计算决定系数，评估性能
predict_score = linregTr.score(x_test, y_test)
print('The decision coeficient is:{:.2f}\n'.format(predict_score))

# 原例题
# 1、数据读取
import pandas as pd
filename = 'c:/data/advertising.csv'
data = pd.read_csv(filename, index_col=0)
x = data.iloc[:, 0:3].values.astype(float)
y = data.iloc[:, 3].values.astype(float)

# 2、将自变量数组和目标变量数组划分为训练集（train）和测试集（test）
from sklearn import model_selection
x_train, x_test, y_train, y_test=model_selection.train_test_split(x, y, test_size=0.35, random_state=1)

# 3、在训练集上学习回归模型linregTr
from sklearn.linear_model import LinearRegression
linregTr=LinearRegression()
linregTr.fit(x_train, y_train)
print(linregTr.intercept_, linregTr.coef_)

# 4、在测试集上应用模型，计算预测结果，RMSE和决定系数R^2
from sklearn import metrics
y_train_pred = linregTr.predict(x_train)
y_test_pred = linregTr.predict(x_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred)
test_err = metrics.mean_squared_error(y_test, y_test_pred)
print('The man squar error of train and test are:{:.2f},{:.2f}'.format(train_err, test_err))

# 5、在测试集上计算决定系数，评估性能
predict_score = linregTr.score(x_test, y_test)
print('The decision coeficient is:{:.2f}'.format(predict_score))
print('结论分析：因为0.92>0.91，所以练习一里的回归模型的拟合效果更好')

print('\n\n思考与练习2')
print('使用100条样本')
# ①读取文件数据至DateFrame的data中②提取前五条
# （序号和销量无关，读取时作为行索引，不用于建模）
import pandas as pd
filename='c:/data/advertising.csv'
data=pd.read_csv(filename, nrows=100, index_col=0)

# 将自变量数组和目标变量数组划分为训练集（train）和测试集（test）
from sklearn import model_selection
x_train, x_test, y_train, y_test=model_selection.train_test_split(x, y, test_size=0.35, random_state=1)

x = data.iloc[:, 0:3].values.astype(float)# 定义x
y = data.iloc[:, 3].values.astype(float)# 定义y
# 学习回归模型linregHalf

from sklearn.linear_model import LinearRegression# 导入模型
linregHalf=LinearRegression()# 初始化模型
linregHalf.fit(x, y)# 输入数据，学习模型
print(linregHalf.intercept_, linregHalf.coef_) # 输出线性回归模型的“截距”，“回归系数”

import joblib # 导入joblib这个提供轻量级流水线的工具
joblib.dump(linregHalf, 'linreg1.pkl') # 将回归模型保存至文件中

# 重新加载模型预测数据
import numpy as np
load_linregHalf = joblib.load('linreg1.pkl') # 从文件读取模型
new_x = np.array([[130.1, 87.8, 69.2]]) # 二维数组
print("6月广告投入：", new_x)
print("预期销售：", load_linregHalf.predict(new_x)) # 用模型预测

print('\n使用200条样本')
import pandas as pd
filename = 'c:/data/advertising.csv'
data = pd.read_csv(filename, nrows=200, index_col=0)
from sklearn import model_selection
x_train, x_test, y_train, y_test=model_selection.train_test_split(x, y, test_size=0.35, random_state=1)
x = data.iloc[:, 0:3].values.astype(float)
y = data.iloc[:, 3].values.astype(float)
from sklearn.linear_model import LinearRegression
linregHalf=LinearRegression()
linregHalf.fit(x, y)
print(linregHalf.intercept_, linregHalf.coef_)
import joblib
joblib.dump(linregHalf, 'linreg2.pkl')
import numpy as np
load_linregHalf = joblib.load('linreg2.pkl')
new_x = np.array([[130.1, 87.8, 69.2]])

print("6月广告投入：", new_x)
print("预期销售：", load_linregHalf.predict(new_x))
print('分析结论：使用200条数据的结论更加可信')
