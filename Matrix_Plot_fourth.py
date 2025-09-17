import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ----------------------------------------------------------------
# Matrix plot
# within the matrix plot i ave to learn about the 
# Heat map
# Cluster map
# Pivot table Heat map

# -----------
# Heat map

flights = sns.load_dataset('flights')
# print(flights)

tips = sns.load_dataset('tips')
# print(tips)

# for creating a heat map we have to know about the corelation
# for calculating a corelation 
# first i have to calculate the covarience and standard deviation from the data
# and then corelation = covarience / standard deviation

tipscorr = tips[['total_bill', 'tip', 'size']]
# print(tipscorr)

# print(tipscorr.corr())

# for creating a heat map
# sns.heatmap(tipscorr.corr(), annot=True)
# plt.show()


# for creating a cluster map
# sns.clustermap(tipscorr.corr())
# plt.show()

# pivot flight
pvtflights = flights.pivot_table(values='passengers', index='month', columns='year')
# print(pvtflights)

sns.heatmap(pvtflights)
plt.show()



