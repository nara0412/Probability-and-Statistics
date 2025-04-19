import scipy.stats
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Z檢定 Coffee
# file = pd.read_excel('Coffee.xlsx', index_col = 0 ,usecols = [1])
# t1 = 0
# n = len(file)
# for i in file.index:
#     t1 += i
# xBar = t1 / n
# mu = 3
# se = 0.18 / (n**0.5)
# zScore = (xBar - mu) / se
# pVal = scipy.stats.norm.cdf(zScore) #單尾檢定 若用雙尾要*2
# print(zScore,pVal)

#Z檢定 Golf
file = pd.read_excel('GolfTest.xlsx', index_col= 0, usecols = [0])
t1 = 0
n = len(file)
for i in file.index:
    t1 += i
xBar = t1 / n
mu = 295
se = 12 / (n**0.5)
zScore = (xBar - mu) / se
pVal = scipy.stats.norm.sf(abs(zScore))*2
print(zScore,pVal)