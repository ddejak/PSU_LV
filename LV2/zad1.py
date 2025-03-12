#Pomoću funkcija numpy.array i matplotlib.pyplot pokušajte nacrtati sljedeću sliku:

import numpy as np
import matplotlib.pyplot as plt 


x = np.array([1,2,3,3,1])
y = np.array([1,2,2,1,1])

plt.plot(x,y, "k", linewidth=2, marker="x", markersize=5)
plt.axis([0,4,0,4])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("OBLIK")
plt.show()