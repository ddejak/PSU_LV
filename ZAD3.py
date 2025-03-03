#Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
#navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
#srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
#Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
#ispiše odgovarajuću poruku.


lista=[]
i=0

while True:
    
    a=input("Unesite broj(Done za kraj petelje): ")
    
    if a == "Done":
       break
    elif a!=str:
        lista.append(int(a))
        i+=1
    
print(lista)
print(max(lista))
print(min(lista))

srednja_v = sum(lista)/i

print(srednja_v)