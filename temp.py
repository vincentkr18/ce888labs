# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib
#matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.interactive(False)
#if __name__ == "__main__":

df = pd.read_csv('M:\\ce888labs\\lab2\\lab2\\vehicles.csv')

data = np.random.rand(10)
print(data)


import numpy as np
import numpy.random as npr
import pylab



def bootstrap(sample, sample_size, iterations):
     mean = []
     for i in range(iterations):
          ll = np.random.choice(sample , size= sample_size, replace=True)
          mean.append(ll.mean())
    # print(mean)   
     stat = np.sort(mean)
     data_mean = stat.mean()
     upper = np.percentile(stat, 95, axis=0)
     lower = np.percentile(stat, 5, axis=0)
     return (data_mean,upper,lower)
 
data_mean,upper,lower = bootstrap(data, 8, 2000)
print(upper)
print(lower)
print(data_mean)
    
print(df.head())

print(df['Current fleet'].mean())
print(df['New Fleet'].mean())

print(df.shape)

data_mean,upper,lower = bootstrap(df['Current fleet'].values, 200,1000)
data_mean_2,upper_2,lower_2 = bootstrap(df['New Fleet'].dropna().values, 150, 4000)
print(upper)
print(lower)
print(data_mean)
print(upper_2)
print(lower_2)
print(data_mean_2)
    