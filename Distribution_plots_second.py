# Distribution plots are visualize the distribution of Quantitative data

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')
# print(data)

# ----------------------------------------------------------------------------------------------------------
# now i will see that how many columns are Qualitative and Quantitative
# so columns like total_bill, tip are Quantitative 
# so i can visualize this using the Distribution plots
# wait let see for the column name - size

# using the code  
# print(data['size'].unique()) # [2 3 4 1 6 5]

# in this data size column is a Qualitative so it cannot be visualize by the distribution plots

# ----------------------------------------------------------------------------------------------------------
# for creating a Distribution plot
# sns.displot(data['total_bill'],bins=50,kde=True)
# sns.displot(data['tip'],bins=50,kde=True)
# plt.show()

# ----------------------------------------------------------------------------------------------------------
# joinplot
# sns.jointplot(x = 'total_bill', y = 'tip', data = data, kind = 'scatter')
# sns.jointplot(x='total_bill', y='tip', data=data, kind='kde')
# sns.jointplot(x='total_bill', y='tip', data=data, kind='hist')
# sns.jointplot(x='total_bill', y='tip', data=data, kind='hex')
# sns.jointplot(x='total_bill', y='tip', data=data, kind='reg')
# sns.jointplot(x='total_bill', y='tip', data=data, kind='resid')
# plt.show()

# ----------------------------------------------------------------------------------------------------------
# pairplot
# sns.pairplot(data)
# now divide it into category wise
# sns.pairplot(data, hue='sex')
# plt.show()

# ---------------------------------------------------------------------------------------------------------
# rugplot
sns.rugplot(data)







