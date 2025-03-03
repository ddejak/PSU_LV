#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
#ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
#riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.


putanja = "C:\\Users\\student\\Desktop\\LV1-20250303\\song.txt"

rijecnik = {}

fhand = open(putanja)

for line in fhand:
    rijec = line.split()
    
    if rijec in rijecnik:
        rijecnik[rijec]+=1
    else:
        rijecnik[rijec]=0
        
print(rijecnik)



fhand.close()