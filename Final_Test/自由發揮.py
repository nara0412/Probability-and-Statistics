import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
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

data = file[['1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13','1_14','3_4']]
data = pd.DataFrame(data)
data = data.mask((data == 999) | (data == 888) | (data == 777))

# 台中和非台中1~14題的資料
Taichung_data = data[data['3_4'] == 1].drop('3_4', axis=1)
otherArea_data = data[(data['3_4'] != 1)].drop('3_4', axis=1)

man_melted = pd.melt(man_data)
woman_melted = pd.melt(woman_data)

# sns.violinplot(data=man_data)
# plt.show()
# sns.violinplot(data=woman_data)
# plt.show()

# sns.violinplot(data=man_data, facecolor='blue', alpha=0.5)
# sns.violinplot(data=woman_data, facecolor='pink', alpha=0.5)
# plt.show()

Taichung_melted = pd.melt(Taichung_data)
otherArea_melted = pd.melt(otherArea_data)

# sns.violinplot(data=Taichung_data)
# plt.show()
# sns.violinplot(data=other_data)
# plt.show()

sns.violinplot(data=Taichung_data, facecolor='blue', alpha=0.5)
sns.violinplot(data=other_data, facecolor='pink', alpha=0.5)
plt.show()