print('思考与练习1')
#1、读取5个样本并输出
import pandas as pd
from sklearn import metrics
filename='c:/data/bankdebt.csv'
data=pd.read_csv(filename,nrows=5,index_col=0,header=None)

#2、训练分类器：将样本中字符类型替换为数字
data=pd.read_csv(filename,index_col=0,header=None)
data.loc[data[1]=='Yes',1]=1
data.loc[data[1]=='No',1]=0
data.loc[data[4]=='Yes',4]=1
data.loc[data[4]=='No',4]=0
data.loc[data[2]=='Single',2]=1
data.loc[data[2]=='Married',2]=2
data.loc[data[2]=='Divorced',2]=3
print(data.loc[1:5,:])

#3、①data前三列是特征属性值，赋给X②data后一列是分类值（整数），赋给y③训练分类器
x=data.loc[:,1:3].values.astype(float)
y=data.loc[:,4].values.astype(int)
#划分为训练集（train）和测试集（test）
from sklearn import model_selection
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.35,random_state=1)
from sklearn import tree#导入决策树，训练分类器
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
clf.score(x_test,y_test)#分类器中score()→得到分类器的Accuracy

#对分类器性能进行评估
predicted_y=clf.predict(x)
from sklearn import metrics
print(metrics.classification_report(y,predicted_y))
print('Confusion matrix:')#混淆矩阵
print(metrics.confusion_matrix(y,predicted_y))

print('\n思考与练习2')
import pandas as pd
from sklearn import metrics
filename='c:/data/bankdebt.csv'
data=pd.read_csv(filename,nrows=5,index_col=0,header=None)
print(data)

data=pd.read_csv(filename,index_col=0,header=None)
data.loc[data[1]=='Yes',1]=1
data.loc[data[1]=='No',1]=0
data.loc[data[4]=='Yes',4]=1
data.loc[data[4]=='No',4]=0
data.loc[data[2]=='Single',2]=1
data.loc[data[2]=='Married',2]=2
data.loc[data[2]=='Divorced',2]=3
print(data.loc[1:5,:])

x=data.loc[:,1:3].values.astype(float)
y=data.loc[:,4].values.astype(int)
from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
clf.score(x,y)

predicted_y=clf.predict(x)
from sklearn import metrics
print(metrics.classification_report(y,predicted_y))
print('Confusion matrix:')
print(metrics.confusion_matrix(y,predicted_y))


#import joblib
#导入joblib这个提供轻量级流水线的工具
#joblib.dump(tree,'tree.pkl')#将模型保存至文件中
#重新加载模型预测数据
#import numpy as np
#load_tree=joblib.load('tree.pkl')#从文件读取模型
#new_x=np.array(data)#二维数组
#print("预期销售：",load_tree.predict(new_x))#用模型预测


