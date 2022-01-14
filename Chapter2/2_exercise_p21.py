# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:26:54 2020

@author: azq
"""

import numpy as np
names=np.array(['王微','肖良英','方绮雯','刘旭阳','钱易铭'])
subjects=np.array(['Math','English','Python','Chinese','Art','Database','Physics'])
scores=np.array([[70,85,77,90,82,84,89],
                 [60,64,80,75,80,92,90],
                 [90,93,88,87,86,90,91],
                 [80,82,91,88,83,86,80],
                 [88,72,78,90,91,73,80]])
print(subjects[[1,2,4]])
print(names[1:5])
print(subjects[2:5])
mask=(subjects=='English')|(subjects=='Physics')
print(subjects[mask])


print(scores[[1,4]])#选取序号为1和4的行
print(scores[[0,3]])#选取第1行和第4行
print(scores[2:5:2,[0,2]])
print(scores[:,[0,4]])

print(np.arange(10,20).reshape(2,5))