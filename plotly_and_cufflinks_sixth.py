import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import cufflinks as cf
from plotly.offline import iplot

tips = sns.load_dataset('tips')

a = tips['total_bill'].iplot(kind='hist')
a.figure.show()







