#Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
#1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
#broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.


try:
    
    a=float(input("Unesite izmedu 0.0 - 1.0:"))
    
    if a < 0.0 or a > 1.0:
        print("Greska")
    
    elif a >=0.9:
        print("A")
    elif a >= 0.8:
        print("B")
    elif a >=0.7:
        print("c")
    elif a >= 0.6:
        print("D")
    elif a < 0.6:
        print("F")
    
    
    
    
except:
    print("Pogrešan unos!!")