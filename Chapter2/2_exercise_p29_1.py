# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:32:17 2020

@author: azq
"""

import numpy as np
names=np.array(['大润发','沃尔玛','好德','农工商'])
fruits=np.array(['苹果','香蕉','橘子','芒果'])

prices=np.random.randint(4,11,size=(4,4))
print(prices)

a=prices[names=='大润发',fruits=='苹果']+1
b=prices[names=='好德',fruits=='香蕉']+1
print(a,b)

c=prices[(names=='农工商')]-2
print(c)

d=prices[(fruits=='苹果')].mean()
e=prices[(fruits=='芒果')].mean()
print(d,e)

print(names[prices[fruits=='橘子'].argmax()])