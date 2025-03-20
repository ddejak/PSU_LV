#Za mtcars skup podataka napišite programski kod koji će odgovoriti na sljedeća pitanja:
# 1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
# 2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
# 3. Kolika je srednja potrošnja automobila sa 6 cilindara?
# 4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
# 5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
# 6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
# 7. Kolika je masa svakog automobila u kilogramima?




import pandas as pd
import numpy as np

mtcars=pd.read_csv("mtcars.csv")

#1
sortmpg=mtcars.sort_values(by="mpg")
print(sortmpg.head(5))

#2
cil8=mtcars[mtcars.cyl == 8]
cil8=cil8.sort_values(by="mpg",ascending=False)
print(cil8.head(3))

#3
cil6=mtcars[mtcars.cyl == 6]
cil6=cil6.iloc[:,1:2]
print(cil6.mean())

#4
cil4lagani = mtcars[(mtcars.cyl == 4) & (mtcars.wt *1000 >= 2000 )  & (mtcars.wt*1000 <=2200)]
cil4lagani = cil4lagani.iloc[:,1:2]
print(cil4lagani.mean())

#5
mjenjaci = mtcars['am'].value_counts()
print(mjenjaci)
print(f"\nAutomatski: {mjenjaci[1]}, Ručni: {mjenjaci[0]}")




#6 Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?

auto_over_100hp = mtcars[(mtcars['am'] == 1) & (mtcars['hp'] > 100)]
print(f"\nBroj automobila s automatskim mjenjačem i snagom preko 100 HP: {len(auto_over_100hp)}")


#7 Kolika je masa svakog automobila u kilogramima?

print("\nMasa svakog automobila u kg:")
cars=mtcars["wt"]*1000 / 2.204
print(cars)