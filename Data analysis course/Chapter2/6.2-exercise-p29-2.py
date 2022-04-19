'''随机游走：使用ndarray和随机数生成函数模拟一个物体在三维空间随机游走的过程
1)创建3*10的二维数组，记录物体每步在三个轴向上的移动距离
每个轴向的移动距离服从标准正态分布（期望0，方差1）
行序0，1，2分别对应x,y,z轴
2）计算每步走完后物体在三维空间的位置
3）计算每步走完后物体到原点的距离（2位小数）
4）统计物体在z轴上到达的最远距离
5）统计物体在三维空间距离原点的最近值
'''
import numpy as np
steps = 10
rndwlk = np.random.normal(0, 1, size=(3, steps))
position = rndwlk.cumsum(axis=1)
x = position[0]
y = position[1]
z = position[2]
print('\n每步走完后物体在三维空间的位置:')
print(position)
dists = np.sqrt(position[0]**2+position[1]**2+position[2]**2)
np.set_printoptions(precision=2)
print('\n每步走完后物体到原点的距离:')
print(dists)
print('\n物体在z轴上到达的最远距离：%f' % abs(position[2]).max())
print('\n物体在三维空间距离原点的最近值：%f' % dists.min())
