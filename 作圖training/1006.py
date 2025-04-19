import matplotlib.pyplot as plt
import numpy as np

x = [2,5,1,3,4,1,5,3,4,2]
y = [50,57,41,54,54,38,63,48,59,46]

plt.xlabel("Number of Commercials")
plt.ylabel("Sales($100s)")
plt.scatter(x,y)
a = np.polyfit(x,y,1)
b = np.poly1d(a)
plt.plot(x,b(x),color='c')
plt.show()