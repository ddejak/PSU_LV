#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. 
#Ova datoteka sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. Primjer dijela datoteke:
#ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
#ham Ok lar... Joking wif u oni...
#spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
#ham Yup next stop.
#a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u porukama koje su tipa spam.
#b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?

putanja = "C:\\Users\\student\\Desktop\\LV1-20250303\\SMSSpamCollection.txt"

fhand = open(putanja)

broj_ham = 0
broj_spam = 0
ukupno_rijeci_ham = 0
ukupno_rijeci_spam = 0
spam_sa_usklicnikom = 0

for line in fhand:
    podaci = line.strip().split("\t")  
    if len(podaci) < 2:  
        continue  
    
    oznaka = podaci[0]
    poruka = podaci[1]
    broj_rijeci = len(poruka.split())

    if oznaka == "ham":
        broj_ham += 1
        ukupno_rijeci_ham += broj_rijeci
    elif oznaka == "spam":
        broj_spam += 1
        ukupno_rijeci_spam += broj_rijeci
        if poruka.endswith("!"):
            spam_sa_usklicnikom += 1

fhand.close()


prosjek_ham = ukupno_rijeci_ham / broj_ham if broj_ham > 0 else 0
prosjek_spam = ukupno_rijeci_spam / broj_spam if broj_spam > 0 else 0

print(f"Prosječan broj riječi u ham porukama: {prosjek_ham:.2f}")
print(f"Prosječan broj riječi u spam porukama: {prosjek_spam:.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {spam_sa_usklicnikom}")
