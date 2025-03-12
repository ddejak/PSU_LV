#Na temelju primjera 2.5. učitajte sliku 'tiger.png'. Manipulacijom odgovarajuće numpy matrice pokušajte:
#a) posvijetliti sliku (povećati brightness),
#b) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
#c) zrcaliti sliku,
#d) smanjiti rezoluciju slike x puta (npr. 10 puta),
#e) prikazati samo drugu četvrtinu slike po širini, a prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biti
#crni.

import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img*1.5, cmap="gray")
plt.show()
plt.imshow(np.rot90(img)*1.5, cmap="gray")
plt.show()
plt.imshow(np.flip(img), cmap="gray")
plt.show()
plt.imshow(img[:,200:401], cmap="gray")
plt.show()
