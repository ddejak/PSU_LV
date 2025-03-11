#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
#ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
#riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.


putanja = "C:\\Users\\student\\Desktop\\LV1-20250303\\song.txt"

rijecnik = {}

fhand = open(putanja)

for line in fhand:
    line = line.strip().lower()  
    rijeci = line.split()  

    for rijec in rijeci:
        if rijec in rijecnik:
            rijecnik[rijec] += 1
        else:
            rijecnik[rijec] = 1

fhand.close()


rijeci_jednom = []

for rijec, broj in rijecnik.items():
    if broj == 1:
        rijeci_jednom.append(rijec)

print(f"Broj riječi koje se pojavljuju samo jednom: {len(rijeci_jednom)}")
print("Te riječi su:", rijeci_jednom)
