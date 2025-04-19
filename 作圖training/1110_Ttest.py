from scipy.stats import ttest_1samp
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = pd.read_excel('FedEmail.xlsx')

mu_0 = 100
alpha = 0.05

t, p_value = ttest_1samp(file, mu_0, alternative='greater')

print(f't統計 =  {t}')
print(f'p_value = {p_value}')