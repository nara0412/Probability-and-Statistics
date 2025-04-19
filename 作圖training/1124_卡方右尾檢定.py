import scipy.stats
import pandas as pd
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = pd.read_excel('BusTimes.xlsx')

known_variance = 4

n = len(file)
df = n-1

sample_variance = np.var(file, ddof=1)
chi_square_statistic = (n - 1) * sample_variance / known_variance

p_value = scipy.stats.chi2.sf(chi_square_statistic, df)

print(chi_square_statistic)
print(p_value)



