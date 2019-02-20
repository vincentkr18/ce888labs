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

df = pd.read_csv('C:\\Users\\vk18602\\PycharmProjects\\Lab2\\vehicles.csv')

data = np.random.rand(500)
print(data)


import numpy as np
import numpy.random as npr
import pylab

num_samples = 400

def bootstrap(data, num_samples, statistic, alpha):
    """Returns bootstrap estimate of 100.0*(1-alpha) CI for statistic."""
    n = len(data)
    idx = npr.randint(0, n, (num_samples, n))
    samples = data[idx]
    stat = np.sort(statistic(samples, 1))
    return (stat[int((alpha/2.0)*num_samples)],
            stat[int((1-alpha/2.0)*num_samples)])

data = np.array([1, 2, 3, 1000, 5])
low, high = bootstrap(data, 100000, np.mean, 0.05)


data = np.random.rand(10)


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
     return (upper,lower)
 
upper,lower = bootstrap(data, 8, 2000)
print(upper)
print(lower)
    
     
    
l = np.array([1, 2, 1, 4, 1])
ll = np.random.choice(l, size=3, replace=True)
print(ll.mean())
np.percentile(l, 5, axis=0)



