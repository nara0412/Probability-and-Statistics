import statsmodels.api as sm
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = pd.read_excel('Group 4.xlsx')

data = file[['1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13','1_14']]
data = pd.DataFrame(data)
data = data.mask((data == 999) | (data == 888) | (data == 777))

# 根據該行的平均數填補缺失的值
def fillna_mean(r):
    return r.fillna(r.mean())
data = data.apply(lambda r: fillna_mean(r), axis=1)

# X = sm.add_constant(data[['1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13']])
X = sm.add_constant(data[['1_2','1_9','1_13']])
Y = data['1_14']

model = sm.OLS(Y, X).fit()

print(model.summary())


