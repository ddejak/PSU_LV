#Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu
#  i nalazi se između 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih 
# uvjeta:

#Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
#  Također, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.


try:
    ocjena=float(input("Unesite ocjenu: "))
    if ocjena<0.0 or ocjena>1.0:
        print("Ocjena mora biti između 0.0 i 1.0")
    elif ocjena>=0.9:
        print("A")
    elif ocjena>=0.8:
        print("B")
    elif ocjena>=0.7:
        print("C")
    elif ocjena>=0.6:
        print("D")
    else:
        print("F")

except:
    print("Greška! Unesite broj između 0.0 i 1.0")

