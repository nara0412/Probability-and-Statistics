import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv("iris.csv")

#h1
freq_table = pd.crosstab(data.species, 'no_of_Brand')
print(freq_table)

#h2
x = data.species.unique()
print(x)
height = data.species.value_counts()
data_search = pd.DataFrame(height, index=x)
#print(data_search)
data_search.plot(kind='bar' , subplots=True , figsize=(8,8) )
data_search.plot(kind='pie' , subplots=True , figsize=(8,8) )
plt.show()

#h3
plt.hist(data['sepal_length'],bins='auto')
plt.hist(data['sepal_width'],bins='auto')
plt.hist(data['petal_length'],bins='auto')
plt.hist(data['petal_width'],bins='auto')
plt.show()