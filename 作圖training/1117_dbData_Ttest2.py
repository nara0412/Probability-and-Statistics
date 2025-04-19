from scipy.stats import ttest_1samp
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pd.read_excel('Matched.xlsx')

data_len = len(data)
d = []
for i in range(data_len):
    d.append(data['Method 1'][i] - data['Method 2'][i])
dBar = (sum(data['Method 1']) - sum(data['Method 2']) ) / data_len

d_sigma = 0.335

mu_d = 0
t_value = (dBar - mu_d) / (d_sigma / (data_len**0.5))
t_value, p_value = ttest_1samp(d, mu_d, alternative='two-sided')
print(f't值: {t_value}\np值: {p_value}')
