from datetime import datetime

#       Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám)
class Szoba:
    def __init__(self,szobaszam,szobaar):
        self.szobaszam=szobaszam
        self.szobaar=szobaar

#       ● Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.(5 pont)
class EgyagyasSzoba(Szoba):
    def __init__(self,szobaszam, extra):
        super().__init__(szobaszam,39000)
        self.extra=extra

class KetagyasSzoba(Szoba):
    def __init__(self,szobaszam,kilatas):
        super().__init__(szobaszam, 53000)
        self.kilatas=kilatas

#       ● Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól) (10 pont)
class Foglalas:
    def __init__(self,szoba,datum):
        self.szoba=szoba
        self.datum=datum


#       ● Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.) (10 pont)
class Szalloda:
    def __init__(self,nev):
        self.nev=nev
        self.szobak = []
        self.foglalasok=[]

    def uj_szoba(self,szoba):
        self.szobak.append(szoba)

#       ● Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. (15 pont)
    def foglalas(self,szobaszam,datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam==szobaszam and foglalas.datum==datum:
                print("\nA szoba már foglalt ezen a napon. \nVálasszon másik szobát vagy másik dátumot!")
                return
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam==szobaszam and foglalas.datum==datum:
                return
        for szoba in self.szobak:
            if szoba.szobaszam==szobaszam:
                self.foglalasok.append(Foglalas(szoba,datum))
                return szoba.szobaar
        print("\nA megadott szobaszám nem létezik a szállodában.")


#       ● Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását. (5 pont)
    def lemondas(self,szobaszam,datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam==szobaszam and foglalas.datum==datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

#       ● Implementálj egy metódust, ami listázza az összes foglalást. (5 pont)
    def listazas(self):
        for foglalas in self.foglalasok:
            print(f"Szoba {foglalas.szoba.szobaszam}, Ipőpont: {foglalas.datum}")

#       ● Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás). (20 pont)
#       ● Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik. (10 pont)

   #Szálloda neve:
szalloda=Szalloda("Hotel Oxford")
#Elérhető szobák:
szalloda.uj_szoba(EgyagyasSzoba(101,["Wifi","TV","Minibár"]))
szalloda.uj_szoba(EgyagyasSzoba(102,["Wifi", "TV", "Minibár","Erkély"]))
szalloda.uj_szoba(KetagyasSzoba(201,["Tengerre néző","Erkély"]))

#Foglalások:
szalloda.foglalas(101, datetime(2024,7,12))
szalloda.foglalas(102, datetime(2024,7,15))
szalloda.foglalas(101, datetime(2024,7,21))
szalloda.foglalas(201, datetime(2024,7,18))
szalloda.foglalas(201, datetime(2024,7,20))
while True:

    print("\n\nÜdvözli a Hotel Oxford!\n\nNavigációs menü:")
    print("1. Szobák listája")
    print("2. Foglalások listázása")
    print("3. Szoba foglalás")
    print("4. Foglalás lemondása")
    print("x. Kilépés")
    print("Fontos közlemény: jelenleg csak egy napra lehetséges a foglalás!")
    option=input("Válasszon a fenti menüpontok közül (pl. '4' a szobák listájához vagy 'x' a kilépéshez): ")
    if option == '1':
        print("Szobák száma: ")
        print(len(szalloda.szobak))
        print("Egyágyas szobák: ")
        for szoba in szalloda.szobak:
            if isinstance(szoba, EgyagyasSzoba):
                print(f"Szobaszám: {szoba.szobaszam}, Ára: {szoba.szobaar}, Extrák: {szoba.extra}")
        print("\nKétágyas szobák: ")
        for szoba in szalloda.szobak:
            if isinstance(szoba, KetagyasSzoba):
                print(f"Szobaszám: {szoba.szobaszam}, Ára: {szoba.szobaar}, Extrák: {szoba.kilatas}")

    elif option == '2':
        print("\nÉlő foglalások:")
        szalloda.listazas()

    elif option == '3':
        szobaszam = int(input("Adja meg a kívánt szoba számát: "))
        datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN)")
#    ● A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor. (10 pont)
        try:
            datum=datetime.strptime(datum,"%Y-%m-%d")
            if datum < datetime.now():
                print("\nA foglalás csak jövőbeni időpontra lehetséges, kérem adjom meg másik időpontot!")
            else:
                szobaar=szalloda.foglalas(szobaszam,datum)
                if szobaar:
                    print(f"Sikeres foglalás! A szoba ára: {szobaar} Ft")
#                else:
#                    print("Az időpont vagy szoba már foglalt!")
        except ValueError:
            print("Érvénytelen szobaszám vagy dátum")

    elif option == '4':
        szobaszam = int(input("Adja meg a lemondani kívánt foglalás szoba számát: "))
        datum = input("Adja meg a foglalás időpontját (ÉÉÉÉ-HH-NN): ")
 #    ● Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek. (5 pont)
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = szalloda.lemondas(szobaszam, datum)
            if siker:
                print("\nA foglalás sikeresen lemondva.")
            elif datum < datetime.now():
                print("\nA foglalás lemondása csak jövőbeni időpontra lehetséges, kérem adjom meg másik időpontot!")
            else:
                print("\nNincs ilyen foglalás.")
        except ValueError:
            print("\nHibás dátum formátum!")

    elif option == 'x':
        break
    else:
        print("\nHibás választás! Csak a felsorolt menüpontok közül választhat!")
