import scipy.stats
import pandas as pd
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pd.read_excel('Training.xlsx')
current = data['Current']
proposed = data['Proposed']

# 計算樣本變異數
var_current = np.var(current, ddof=1)
var_proposed = np.var(proposed, ddof=1)

# F值 代表變異數的比值(誰大誰小)
f_value = var_current / var_proposed
# 自由度
df_current = len(current) - 1
df_proposed = len(proposed) - 1

# 雙尾檢定
p_value = 2 * min(scipy.stats.f.cdf(f_value, df_current, df_proposed), 1 - scipy.stats.f.cdf(f_value, df_proposed, df_current))

print(f'f_value = {f_value}')
print(f'p_value = {p_value}')