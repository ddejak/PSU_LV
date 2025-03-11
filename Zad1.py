#Pomoću funkcija numpy.array i matplotlib.pyplot pokušajte nacrtati sljedeću sliku:
#Igrajte se sa slikom, promijenite boju oblika, debljinu linije i sl.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])

plt.plot(x, y, 'rx-', linewidth=0.5)

plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")

plt.xlim(0, 4)
plt.ylim(0, 4)

plt.show()
