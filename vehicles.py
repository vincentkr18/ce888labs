import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.interactive(False)
#if __name__ == "__main__":

df = pd.read_csv('C:\\Users\\vk18602\\PycharmProjects\\Lab2\\vehicles.csv')
print(df.head(10))

sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

sns_plot.axes[0,0].set_ylim(0,)
sns_plot.axes[0,0].set_xlim(0,)

sns_plot.savefig("scaterplot.png",bbox_inches='tight')
sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')
plt.show()
#df.dropna(axis='columns', inplace = True)
#print(df.head(10))

#Anan=A[~np.isnan(A)] # Remove the NaNs

#sns.distplot(Anan,hist=True,bins=10)
#plt.show(block=True)
#plt.interactive(False)
sns_dist = sns.distplot(df['New Fleet'].dropna(), bins=20, kde=False, rug=True).get_figure()
plt.show()
#sns_dist.axes[0,0].set_ylim(0,)
#sns_dist.axes[0,0].set_xlim(0,)

sns_dist.savefig("dist_newfleet.png")
sns_dist.savefig("dist_newfleet.pdf")

sns_cur = sns.distplot(df['Current fleet'].dropna(), bins=20, kde=False, rug=True).get_figure()
plt.show()
#sns_dist.axes[0,0].set_ylim(0,)
#sns_dist.axes[0,0].set_xlim(0,)

sns_cur.savefig("dist_currentfleet.png")
sns_cur.savefig("dist_currentfleet.pdf")


