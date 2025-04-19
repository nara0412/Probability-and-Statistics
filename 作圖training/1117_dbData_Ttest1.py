from scipy.stats import ttest_ind
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pd.read_excel('SoftwareTest.xlsx')
a_data = data['Current']
b_data = data['New']

# #樣本數
a_len = len(a_data)
b_len = len(b_data)

#樣本平均值
a_mu = sum(a_data) / a_len
b_mu = sum(b_data) / b_len

#樣本標準差
a_ssigma = 40
b_ssigma = 44

t_value = (a_mu - b_mu) / (a_ssigma**2 / a_len + b_ssigma**2 / b_len)**0.5
t_value, p_value = ttest_ind(a_data, b_data, alternative='greater')

print(f't值: {t_value}\np值: {p_value}')