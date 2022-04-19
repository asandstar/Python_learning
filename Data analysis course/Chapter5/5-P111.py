
#题目一
import pandas as pd
data=pd.read_csv('c:/data/wine.data',header=None)

#取data前一列作为分类值
x = data.loc[ :,2:14 ].values.astype(float)
y = data.loc[ :,1].values.astype(int)

#训练模型，预测样本分类
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
clf.score(x,y)

#对分类器性能进行评估
predicted_y=clf.predict(x)
from sklearn import metrics
print(metrics.classification_report(y,predicted_y))
print('Confusion matrix:')#混淆矩阵
print(metrics.confusion_matrix(y,predicted_y))

#题目二
#1、数据读取
import pandas as pd
import numpy as np
from pandas import DataFrame,Series

filename='c:/data/housePrice.xlsx'
data=pd.read_excel(filename,index_col=0)

from pylab import mpl 
mpl.rcParams['font.sans-serif']=['SimHei']

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12,12))

plt.subplots_adjust(wspace=0.8,hspace=1.3)

ax1=fig.add_subplot(2,2,1)
data.plot(kind='scatter',x='建筑面积',y='价格（万）',label='（建筑面积，价格）',figsize=(12,12),alpha=0.7,ax=ax1)
plt.title('建筑面积-价格')
plt.grid()
ax2=fig.add_subplot(2,2,2)
zhuang=data.groupby(['装修'])
grouped=zhuang.aggregate({'价格（万）':np.mean})
grouped.plot(kind='barh',color='c',figsize=(12,12),ax=ax2)
plt.title('装修方式-价格')

ax3=fig.add_subplot(3,2,3)
dianti=data.groupby(['电梯'])
diangrouped=dianti.aggregate({'价格（万）':np.mean})
diangrouped.plot(kind='bar',color='r',figsize=(12,12),ax=ax3)
plt.title('电梯——价格')




ax4=fig.add_subplot(3,2,4)
jiegou=data.groupby(['建筑结构'])
jgrouped=jiegou.aggregate({'价格（万）':np.mean})
jgrouped.plot(kind='barh',color='g',figsize=(12,12),ax=ax4)
plt.title('建筑结构——价格')

ax5=fig.add_subplot(3,2,5)
censhu=data.groupby(['所处层数'])
cengrouped=censhu.aggregate({'价格（万）':np.mean})
cengrouped.plot(kind='bar',color='m',figsize=(12,12),ax=ax5)
plt.title('所处层数——价格')

ax6=fig.add_subplot(3,2,6)
zong=data.groupby(['总楼层'])
zgrouped=zong.aggregate({'价格（万）':np.mean})
zgrouped.plot(kind='barh',color='b',figsize=(12,12),ax=ax6)
plt.title('总楼层——价格')

data.drop(['朝向','地址','小区','经度','纬度','建筑类型'],axis=1,inplace=True)
data.loc[data['装修']=='精装','装修']=1
data.loc[data['装修']=='简装','装修']=2
data.loc[data['装修']=='毛坯','装修']=3
data.loc[data['装修']=='其他','装修']=4
data.loc[data['电梯']=='无','电梯']=0
data.loc[data['电梯']=='有','电梯']=1
data.loc[data['所处层数']=='低','所处层数']=1
data.loc[data['所处层数']=='中','所处层数']=2
data.loc[data['所处层数']=='高','所处层数']=3
data.loc[data['建筑结构']=='一梯两户','建筑结构']=1
data.loc[data['建筑结构']=='两梯四户','建筑结构']=2
data.loc[data['建筑结构']=='一梯三户','建筑结构']=3


#学习回归模型linregTr
from sklearn.linear_model import LinearRegression
x=data.iloc[:,0:11].values
y=data.iloc[:,11].values
linreg=LinearRegression()
linreg.fit(x,y)
print(linreg.intercept_,linreg.coef_)

import joblib
joblib.dump(linreg,'houseprice_linreg.pkl')
load_houseprice_linreg=joblib.load('houseprice_linreg.pkl')
new_X=np.array([[3,1,1,1,123.23,1,0,5,1,2,2010]])
print('预测价格是：')
print(load_houseprice_linreg.predict(new_X))


