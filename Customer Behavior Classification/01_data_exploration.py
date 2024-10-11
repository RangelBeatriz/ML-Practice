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
    f.set_title(df_plot.columns.values[i - 1])

    vals = np.size(df_plot.iloc[:, i - 1].unique())
    
    plt.hist(df_plot.iloc[:, i - 1], bins=vals, color='#3F5D7D')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(path + '/figures/app_data_hist.png')


#Comment code above to generate the corr_figure
data_fig = df_plot.corrwith(df.enrolled).plot.bar(figsize=(20,10),title = 'Correlation with Response variable', fontsize = 15, rot = 45, grid = True)
data_fig.figure.savefig(path + '/figures/corr_plot.png')

corr = df_plot.corr()

mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True


# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(18, 15))
f.suptitle("Correlation Matrix", fontsize = 40)

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
heatmap = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
heatmap_fig = heatmap.get_figure()
heatmap_fig.savefig(path + '/figures/heatmap.png')