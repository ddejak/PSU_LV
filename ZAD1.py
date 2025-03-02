#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu.
#  Koristite ugrađenu Python metodu input().
#  Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran.
#  Na kraju prepravite rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji
#  naziva total_euro.


sat=float(input("Unesite broj radnih sati: "))
eur_sat=float(input("Unesite koliko je plaćen po radnom satu: "))

def total_euro():
    total=sat*eur_sat
    return total

print("Ukupno ste zaradili: ",total_euro(),"€")