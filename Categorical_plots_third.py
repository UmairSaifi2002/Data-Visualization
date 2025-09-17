# Now i will learn about the Cateorical Plots
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = sns.load_dataset('tips')

# ----------------------------------------------------------------
# learned about countplot
# sns.countplot(x = data['sex'])
# sns.countplot(x = data['sex'], hue=data['smoker'])
# plt.show()

# ----------------------------------------------------------------
# learned about barplot
# sns.barplot(x = data['sex'], y = data['total_bill'])
# plt.show()
# sns.barplot(x = data['sex'], y = data['total_bill'], estimator=np.sum)
# plt.show()
# sns.barplot(x = data['sex'], y = data['tip'], estimator=np.sum)
# plt.show()
# sns.boxplot(x = 'tip', y = 'day', data = data, palette = 'rainbow')
# plt.show()

# ----------------------------------------------------------------
# # voilin plot
# sns.violinplot(x='day', y='total_bill', data=data)
# plt.show()








