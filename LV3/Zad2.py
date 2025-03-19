import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje mtcars skupa podataka
data = pd.read_csv('mtcars.csv')

# 1. Kojih 5 automobila ima najveću potrošnju? (mpg - miles per gallon, manja vrijednost znači veću potrošnju)
top5_potrosnja = data.sort_values(by='mpg', ascending=True).head(5)
print("5 automobila s najvećom potrošnjom:")
print(top5_potrosnja[['car', 'mpg']])

# 2. Tri automobila s 8 cilindara s najmanjom potrošnjom
lowest_8cyl = data[data['cyl'] == 8].sort_values(by='mpg', ascending=False).head(3)
print("\nTri automobila s 8 cilindara s najmanjom potrošnjom:")
print(lowest_8cyl[['car', 'mpg']])

# 3. Srednja potrošnja automobila sa 6 cilindara
avg_mpg_6cyl = data[data['cyl'] == 6]['mpg'].mean()
print(f"\nSrednja potrošnja automobila sa 6 cilindara: {avg_mpg_6cyl:.2f} mpg")

# 4. Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs
filtered_4cyl = data[(data['cyl'] == 4) & (data['wt'] * 1000 >= 2000) & (data['wt'] * 1000 <= 2200)]
avg_mpg_4cyl = filtered_4cyl['mpg'].mean()
print(f"\nSrednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs: {avg_mpg_4cyl:.2f} mpg")

# 5. Broj automobila s ručnim (am=1) i automatskim (am=0) mjenjačem
transmission_counts = data['am'].value_counts()
print(f"\nAutomatski: {transmission_counts[0]}, Ručni: {transmission_counts[1]}")

# 6. Automobili s automatskim mjenjačem i snagom preko 100 konjskih snaga
auto_over_100hp = data[(data['am'] == 0) & (data['hp'] > 100)]
print(f"\nBroj automobila s automatskim mjenjačem i snagom preko 100 KS: {len(auto_over_100hp)}")

# 7. Masa svakog automobila u lbs
print("\nMasa svakog automobila u lbs:")
print(data[['car', 'wt']])

# 1. Barplot potrošnje automobila s 4, 6 i 8 cilindara
avg_mpg_by_cyl = data.groupby('cyl')['mpg'].mean()
plt.bar(avg_mpg_by_cyl.index, avg_mpg_by_cyl.values, color='blue')
plt.title('Prosječna potrošnja automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')
plt.show()

# 2. Boxplot distribucije težine automobila s 4, 6 i 8 cilindara
cylinders = [4, 6, 8]
data_to_plot = [data[data['cyl'] == cyl]['wt'] for cyl in cylinders]
plt.boxplot(data_to_plot, labels=cylinders)
plt.title('Distribucija težine automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (1000 lbs)')
plt.show()

# 3. Usporedba potrošnje između ručnih i automatskih mjenjača
manual_mpg = data[data['am'] == 1]['mpg']
auto_mpg = data[data['am'] == 0]['mpg']
plt.boxplot([auto_mpg, manual_mpg], labels=['Automatski', 'Ručni'])
plt.title('Usporedba potrošnje - Ručni vs. Automatski mjenjač')
plt.xlabel('Mjenjač')
plt.ylabel('Potrošnja (mpg)')
plt.show()

# 4. Odnos ubrzanja i snage automobila za ručni i automatski mjenjač
manual = data[data['am'] == 1]
auto = data[data['am'] == 0]
plt.scatter(manual['hp'], manual['qsec'], color='red', label='Ručni')
plt.scatter(auto['hp'], auto['qsec'], color='blue', label='Automatski')
plt.title('Odnos ubrzanja i snage za ručne i automatske mjenjače')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (qsec)')
plt.legend()
plt.show()
