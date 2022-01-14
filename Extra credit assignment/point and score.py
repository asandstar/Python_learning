import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('C:/data/score.xlsx', index_col='year')
data1 = data[['math1', 'math2', 'math3']]
data1.plot(kind='bar', title='Average scores of 03-19 math', 
           ylim=[50, 95])
plt.savefig('score.jpg', dpi=400, bbox_inches='tight')
data = pd.read_excel('C:/data/point.xlsx', index_col='point')
data.plot(kind='barh', title='probability of points', 
          grid=True, use_index=True)
plt.savefig('point.jpg', dpi=400, bbox_inches='tight')
