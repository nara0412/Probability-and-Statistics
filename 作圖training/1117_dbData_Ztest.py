import scipy.stats
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pd.read_excel('ExamScores.xlsx')

a_data = data['Center A'].dropna()
b_data = data['Center B']

a_len = len(a_data)
b_len = len(b_data)

a_mu = sum(a_data) / a_len
b_mu = sum(b_data) / b_len

a_sigma = 10
b_sigma = 10
alpha = 0.05

zScore = (a_mu - b_mu) / ((a_sigma**2 / a_len + b_sigma**2 / b_len)**0.5)
pVal = scipy.stats.norm.sf(abs(zScore))*2
print(zScore,pVal)
