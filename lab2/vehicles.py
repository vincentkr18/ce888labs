import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./vehicles.csv')
print((df.columns))
print(df.values.T[0])

sns_plot2 = sns.distplot(df.values.T[0], bins=25, kde=False, rug=True).get_figure()

axes = plt.gca()
axes.set_xlabel('Current Fleet')
axes.set_ylabel('Count')

sns_plot2.savefig("histogram_vehicles.png", bbox_inches='tight')
sns_plot2.savefig("histogram_vehicles.pdf", bbox_inches='tight')

plt.clf()

df_new = df.dropna()

print(df_new.values.T[1])

sns_plot1 = sns.distplot(df_new.values.T[1], bins=20, kde=False, rug=True).get_figure()

axes1 = plt.gca()
axes1.set_xlabel('New Fleet')
axes1.set_ylabel('Count')

sns_plot1.savefig("histogram_NewFleet_vehicles.png", bbox_inches='tight')
sns_plot1.savefig("histogram_NewFleet_vehicles.pdf", bbox_inches='tight')
