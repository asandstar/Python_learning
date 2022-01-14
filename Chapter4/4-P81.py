import pandas
import numpy
import matplotlib.pyplot as plt

df = pandas.read_csv('data/bankpep.csv', index_col=None)

plt.rcParams['font.sans-serif'] = ['Times New Roman']

# 1
df_1 = df['age'].copy()
df_1.plot(kind='hist', density=True)
df_1.plot(kind='kde', color='orange')
plt.title('Customer Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

# 2
df_2 = df[['age', 'income']].copy()
df_2.plot(kind='scatter', x='age', y='income')
plt.title('Customer Income')
plt.xlabel('Age')
plt.xlim((0, 80))
plt.ylabel('Income')
plt.legend(['(age,income)'])
plt.grid()
plt.show()

# 3
df_3 = df[['age', 'income', 'children']].copy()
df_3.columns = ['Age', 'Income', 'Children']
pandas.plotting.scatter_matrix(df_3, diagonal='hist')
plt.show()

# 4
df_4 = df[['region', 'income']].copy()
group_4 = df_4.groupby(['region'])
group_4_mean = group_4.aggregate({'income': numpy.mean})
group_4_std = group_4.aggregate({'income': numpy.std})
group_4_mean.plot(kind='bar', color='red', yerr=group_4_std, legend=None, rot=45)
plt.title('Customer Income')
plt.xlabel('Region')
plt.show()


# 5
fig_5 = plt.figure()

ax_5_1 = fig_5.add_subplot(2, 2, 1)
df_5_1 = df.groupby(['sex'])
df_5_1 = df_5_1.aggregate({'sex': pandas.value_counts})
df_5_1.plot(kind='pie', y='sex', autopct='%1.1f%%', startangle=60, legend=None, ax=ax_5_1)
plt.title('Customer Sex')

ax_5_2 = fig_5.add_subplot(2, 2, 2)
mask_5_2 = df['car'] == 'YES'
df_5_2 = df[mask_5_2].copy()
df_5_2 = df_5_2.groupby(['sex', 'car'])
df_5_2 = df_5_2.aggregate({'car': pandas.value_counts})
df_5_2.plot(kind='pie', y='car', autopct='%1.1f%%', startangle=60, legend=None, ax=ax_5_2)
plt.title('Customer Car Sex')

ax_5_3 = fig_5.add_subplot(2, 2, 3)
df_5_3 = df.groupby(['children'])
df_5_3 = df_5_3.aggregate({'children': pandas.value_counts})
df_5_3.plot(kind='pie', y='children', autopct='%1.1f%%', startangle=30, legend=None, ax=ax_5_3)
plt.title('Customer Children')

plt.show()

# 6
df_6 = df[['sex', 'income']].copy()
df_6.boxplot(by='sex')
plt.suptitle('Boxplot grouped by sex income')
plt.title('')
plt.show()
