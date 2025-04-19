from scipy.stats import chi2_contingency
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = pd.read_excel('Group 4.xlsx')

data = file[['1_1','1_2','1_3','1_4','1_5','1_12','3_2','3_3','3_6']]
data = pd.DataFrame(data)
data = data.mask((data == 999) | (data == 888) | (data == 777))

# 中位數填補缺失的值
def fillna_median(r):
    return r.fillna(r.median())
data = data.apply(lambda r: fillna_median(r), axis=1)

column = ['3_2','3_3','3_6','3_6','3_6','3_6','3_6']
row = ['1_12','3_2','1_1','1_2','1_3','1_4','1_5']

chi_value = [ _ for _ in range(7)]
p_value = [ _ for _ in range(7)]

for i in range(7):
    crosstable = pd.crosstab(data[row[i]], data[column[i]])
    chi_value[i], p_value[i], dof, expected_freq = chi2_contingency(crosstable)
    print(f'{column[i]} => 卡方值= {chi_value[i]} , P值 = {p_value[i]}')
    if p_value[i] <= 0.05:
        print(f'crosstable:\n{crosstable}')

final_test_data = pd.DataFrame(
    {
        '列變數': column,
        '行變數': row,
        '卡方值': chi_value,
        'P-value': p_value,
    }

)
final_test_data.to_excel('FinalTest_3.xlsx', index=False)