import pandas as pd
import matplotlib.pyplot as plt
import os

#用os.chdir將Python指定在這個資料夾尋找iris.csv這個檔案
os.chdir(os.path.dirname(os.path.abspath(__file__)))
dataFile = pd.read_csv("iris.csv")

df = pd.DataFrame(dataFile)
df = df.describe()
print(df)

dataPtl = pd.read_csv("iris.csv",usecols=[2,4])
box = pd.DataFrame(dataPtl)
box.boxplot(by='species',figsize=(8,6))
plt.show()