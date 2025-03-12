#U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32
#automobila (modeli 1973-74). Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.
#a) Učitajte datoteku mtcars.csv pomoću:
#data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
#delimiter=",", skiprows=1)
#b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe
#matplotlib.pyplot.scatter.
#c) Na istom grafu prikažite i informaciju o težini pojedinog vozila (npr. veličina točkice neka bude u skladu sa
#težinom wt).
#d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
#e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).


import numpy as np
import matplotlib.pyplot as plt 


data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

mpg=data[:,0]
cyl=data[:,1]
disp=data[:,2]
hp=data[:,3]
drat=data[:,4]
wt=data[:,5]



plt.scatter(mpg,hp,linewidths=wt)
plt.xlabel("MPG")
plt.ylabel("HP")
plt.show()


print(np.max(mpg))
print(np.min(mpg))
print(np.mean(mpg))

mpg_6=[]
hp_6=[]
wt_6=[]

i=-1
for a in cyl:
    i+=1
    if a ==6:
        mpg_6.append(mpg[i])
        hp_6.append(hp[i])
        wt_6.append(wt[i])

        
print(np.max(mpg_6))
print(np.min(mpg_6))
print(np.mean(mpg_6))

