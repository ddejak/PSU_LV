#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
#Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
#rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.
#Primjer:
#Radni sati: 35 h
#eura/h: 8.5
#Ukupno: 297.5 eura


sat = float(input("Unesite radne sate: "))
eur_sat = float(input("Unesite eur/satu: "))

def total_euro():
     total = sat*eur_sat
     return total
total=total_euro()

print("Ukupno: ",total)