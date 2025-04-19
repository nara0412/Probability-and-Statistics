import pandas as pd
import os
from scipy import stats
#用os.chdir將Python指定在這個資料夾尋找AirRating.xlsx這個檔案
os.chdir(os.path.dirname(os.path.abspath(__file__)))

testFile = pd.read_excel("AirRating.xlsx")
results = stats.ttest_1samp(testFile['Rating'],7,alternative='greater') 
#右尾檢定greater H設7
print(results)