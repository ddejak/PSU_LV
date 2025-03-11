import numpy as np
import matplotlib.pyplot as plt

# a) Učitavanje podataka
data = np.loadtxt(open("C:\\Users\\domin\\OneDrive\\Desktop\\Strojno Ucenje\\LV2\\mtcars.csv", "rb"), delimiter=",", skiprows=1, usecols=(1,2,3,4,5,6))

# Ekstrakcija potrebnih varijabli
mpg = data[:, 0]  # Potrošnja goriva (miles per gallon)
hp = data[:, 2]   # Konjske snage (horsepower)
wt = data[:, 4]   # Težina automobila (weight)
cyl = data[:, 1]  # Broj cilindara

# b) Scatter plot: mpg vs hp
plt.figure(figsize=(8,6))
plt.scatter(hp, mpg, s=wt*100, color='b', alpha=0.5, edgecolors='k')
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja goriva (mpg)")
plt.title("Ovisnost potrošnje goriva o konjskim snagama")
plt.grid(True)

# c) Na grafu veličina točke ovisi o težini automobila (wt) već urađeno u b)

# d) Izračun minimalne, maksimalne i srednje vrijednosti potrošnje (mpg)
min_mpg = np.min(mpg)
max_mpg = np.max(mpg)
mean_mpg = np.mean(mpg)
print(f"Minimalna potrošnja: {min_mpg} mpg")
print(f"Maksimalna potrošnja: {max_mpg} mpg")
print(f"Srednja potrošnja: {mean_mpg:.2f} mpg")

# e) Analiza samo za automobile sa 6 cilindara
mpg_6cyl = mpg[cyl == 6]
min_mpg_6 = np.min(mpg_6cyl)
max_mpg_6 = np.max(mpg_6cyl)
mean_mpg_6 = np.mean(mpg_6cyl)
print(f"(6 cilindara) Minimalna: {min_mpg_6} mpg, Maksimalna: {max_mpg_6} mpg, Srednja: {mean_mpg_6:.2f} mpg")

plt.show()
