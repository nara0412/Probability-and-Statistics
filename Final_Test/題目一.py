import scipy.stats as st
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = pd.read_excel('Group 4.xlsx')

data = file[['受訪者性別','1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13','1_14']]
data = pd.DataFrame(data)
data = data.mask((data == 999) | (data == 888) | (data == 777))

# 各性別1~14題的資料
man_data = data[data['受訪者性別'] == 1].drop('受訪者性別', axis=1)
woman_data = data[data['受訪者性別'] == 0].drop('受訪者性別', axis=1)
other_data = data[(data['受訪者性別'] != 1) & (data['受訪者性別'] != 0)].drop('受訪者性別', axis=1)

# 各性別的資料筆數
man_len = len(man_data)
woman_len = len(woman_data)
other_len = len(other_data)
print(f'man = {man_len}\nwoman = {woman_len}\nother = {other_len}')

data = file[['1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13','1_14','3_4']]
data = pd.DataFrame(data)
data = data.mask((data == 999) | (data == 888) | (data == 777))

# 台中和非台中1~14題的資料
Taichung_data = data[data['3_4'] == 1].drop('3_4', axis=1)
otherArea_data = data[(data['3_4'] != 1)].drop('3_4', axis=1)

# 台中和非台中的資料筆數
Taichung_len = len(Taichung_data)
otherArea_len = len(otherArea_data)
print(f'Taichung = {Taichung_len}\notherArea_len = {otherArea_len}')

# 代表1~14題的男女平均值、t值、P值
man_mu = [ _ for _ in range(14)]
woman_mu = [ _ for _ in range(14)]
t_gender = [ _ for _ in range(14)]
p_gender = [ _ for _ in range(14)]

# 代表1~14題的台中和非台中平均值、t值、P值
Taichung_mu = [ _ for _ in range(14)]
otherArea_mu = [ _ for _ in range(14)]
t_area = [ _ for _ in range(14)]
p_area = [ _ for _ in range(14)]

# 針對性別做檢定
for i in range(14):
    num = '1_' + str(i+1)

    # 將該題有漏答或不適用的忽略
    tempdata_1 = man_data[num].dropna().astype('int')
    tempdata_2 = woman_data[num].dropna().astype('int')

    # 忽略後的資料總筆數
    templen_1 = len(tempdata_1)
    templen_2 = len(tempdata_2)

    # t檢定
    t_gender[i], p_gender[i] = st.ttest_ind(tempdata_1, tempdata_2, alternative='two-sided')

    # 平均值
    man_mu[i] = sum(tempdata_1) / templen_1
    woman_mu[i] = sum(tempdata_2) / templen_2

# 針對地區做檢定
for i in range(14):
    num = '1_' + str(i+1)

    # 將該題有漏答或不適用的忽略
    tempdata_1 = Taichung_data[num].dropna().astype('int')
    tempdata_2 = otherArea_data[num].dropna().astype('int')

    # 忽略後的資料總筆數
    templen_1 = len(tempdata_1)
    templen_2 = len(tempdata_2)

    # t檢定
    t_area[i], p_area[i] = st.ttest_ind(tempdata_1, tempdata_2, alternative='two-sided')

    # 平均值
    Taichung_mu[i] = sum(tempdata_1) / templen_1
    otherArea_mu[i] = sum(tempdata_2) / templen_2

final_test_data = pd.DataFrame(
    {
        ' ': ['1_' + str(i+1) for i in range(14)],
        't值': t_gender,
        'P-value': p_gender,
        '男平均':man_mu,
        '女平均':woman_mu,
        '':'',
        '  ': ['1_' + str(i+1) for i in range(14)],
        't值 ': t_area,
        'P-value ': p_area,
        '台中平均': Taichung_mu,
        '非台中平均': otherArea_mu
    }
)

final_test_data.to_excel('FinalTest_1.xlsx', index=False)