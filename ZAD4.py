#Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije oblika:
#Primijenjeno strojno učenje – laboratorijske vježbe – VJEŽBA 1 7
#X-DSPAM-Confidence: <neki_broj>
#koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite
#datoteke mbox.txt i mbox-short.txt
#Primjer
#Ime datoteke: mbox.txt
#Average X-DSPAM-Confidence: 0.894128046745
#Ime datoteke: mbox-short.txt
#Average X-DSPAM-Confidence: 0.750718518519



ime=input("Unesite putanju do datoteke: ")
i=0.0
sum=0.0

fhand=open(ime)

for line in fhand:
   words = line.split()
   
   
   if  "X-DSPAM-Confidence:" in line:
       i+=1
       sum+=float(words[1])
       

print("Average X-DSPAM-Confidence je: ",sum/i)


fhand.close()