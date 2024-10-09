import pandas as pd
import numpy as np
from dateutil import parser
import matplotlib.pyplot as plt
import seaborn as sns
import os

path = os.getcwd()

df = pd.read_csv(path + '/data/appdata10.csv')

print(df.head())

print(df.describe())


df["hour"] = df.hour.str.slice(1, 3).astype(int)

#Creating a dataframe with the values to plot
df_plot = df.copy().drop(columns = ['user', 'screen_list', 'enrolled_date',
                                           'first_open', 'enrolled'])


plt.suptitle('Histograms of Numerical Columns', fontsize=20)
for i in range(1, df_plot.shape[1] + 1):
    plt.subplot(3, 3, i)
    f = plt.gca()
#    f.axes.get_yaxis().set_visible(False)
    f.set_title(df_plot.columns.values[i - 1])

    vals = np.size(df_plot.iloc[:, i - 1].unique())
    
    plt.hist(df_plot.iloc[:, i - 1], bins=vals, color='#3F5D7D')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(path + '/figures/app_data_hist.png')