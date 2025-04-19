import scipy.stats
import pandas as pd
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pd.read_excel('fowle.xlsx', index_col= 0, usecols = [0])
n = len(data)
xBar = 0
for i in data.index:
    xBar += i
xBar = xBar / n
mu = 15
se = 4 / (n**0.5)
zScore = (xBar - mu) / se
p_value = scipy.stats.norm.sf(zScore)
print(f'Z = {zScore}\nP = {p_value}')

file = pd.read_excel('childcare.xlsx')
data = file['Hours Spent in Child Care']
n = len(data)
xBar = 0
for i in data:
    xBar += i
xBar = xBar / n
result = scipy.stats.ttest_1samp(data,6.4,alternative='two-sided')
print(f'xBar = {xBar}\nresult = {result}')

file = pd.read_excel('hotel.xlsx')
data_1 = file['Atlanta'].dropna()
data_2 = file['Houston']
len_1 = len(data_1)
len_2 = len(data_2)
mu_1 = sum(data_1) / len_1
mu_2 = sum(data_2) / len_2
sigma_1 = 20
sigma_2 = 25
zScore = (mu_1 - mu_2) / (((sigma_1**2) / len_1 + (sigma_2**2) / len_2)**0.5)
p_value = scipy.stats.norm.cdf(zScore)
print(f'Z= {zScore}\nP= {p_value}')

file = pd.read_excel('lateflights.xlsx')
data_1 = file['Delta']
data_2 = file['Southwest'].dropna()
xBar_1, xBar_2 = 0,0
for i in data_1:
    xBar_1 += i
for i in data_2:
    xBar_2 += i
xBar_1 = xBar_1 / len(data_1)
xBar_2 = xBar_2 / len(data_2)
print(f'xBar_1 = {xBar_1}\nxBar_2 = {xBar_2}')
result = scipy.stats.ttest_ind(data_1, data_2, alternative='two-sided')
print(result)

file = pd.read_excel('costco.xlsx')
data = file['Satisfaction Score']
n = len(data)
xBar = 0
for i in data:
    xBar += i
xBar = xBar / n
print(f'xBar = {xBar}')

df = n - 1
sigma = 12
sample_variance = np.var(data, ddof=1)
print(f'樣本變異數 {sample_variance}\n樣本標準差 {sample_variance**0.5}')

chi_square = df * sample_variance / (sigma**2)
p_value = scipy.stats.chi2.sf(chi_square, df)*2
print(f'p_value = {p_value}')
