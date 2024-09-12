
def feladat_1_2():
    nev1:str = str(input("Kérlek add meg a vezetékneved: "))
    nev2:str = str(input("Kérlek add meg a keresztneved: "))
    print(f"{nev1} {nev2}")
    print(nev1+" "+nev2)



def feladat_3_4():
    szam1:int = int(input("Adj meg egy számot: "))
    szam1 += 15
    print(f"A megadott számhoz hozzáadtam 15-öt és az értéke ennyi lett: {szam1}")
    szam1 *= 2
    print(f"A 15-el növelt számnak a kétszerese: {szam1}")



def feladat_5():
    atmero = int(input("Kérlek adj meg egy egész számot(kör átmérője lesz): "))
    return atmero

def keruletszamitas(atmero):
    sugar = atmero / 2
    return 2 * 3.14159 * sugar

def teruletszamitas(atmero):
    sugar = atmero / 2
    return 3.14159 * sugar ** 2

def korvegeredmeny(atmero, terulet):
    kerulet = keruletszamitas(atmero)
    terulet = teruletszamitas(atmero)
    print(f"Kör kerülete: {kerulet}")
    print(f"Kör területe: {terulet}")



def feladat_6():
    a = int(input("Kérlek adj meg egy egész számot(teglalap a oldala lesz): "))
    b = int(input("Kérlek adj meg egy egész számot(teglalap b oldala lesz): "))
    return a,b

def keruletszamitas2(a,b):
    return 2 * (a + b)


def teruletszamitas2(a, b):
    return a * b

def teglalaperedmeny(a,b):
    kerulet = keruletszamitas2(a,b)
    terulet = teruletszamitas2(a,b)
    print(f"Téglalap kerülete: {kerulet}")
    print(f"Téglalap területe: {terulet}")



def feladat_7():
    szam1 = int(input("Adj meg egy számot: "))
    szam2 = int(input("Adj meg egy számot: "))
    szam3 = int(input("Adj meg egy számot: "))
    return szam1,szam2,szam3

def mertaniszamolas(szam1,szam2,szam3):
    atlag = (szam1 + szam2 + szam3) / 3
    return atlag

def mertanieredmeny(atlag):
    print(f"A számtani közép: {atlag}")

    

def feladat8():
    a:int = int(input("Kérlek add meg az egyik befogót: "))
    b:int = int(input("Kérlek add meg a másik egyik befogót: "))
    return a,b

def haromszogszamolas(a,b):
    cc = a*a + b*b
    c = cc**0.5
    return c

def haromszogeredmeny(c):
    print(f"A háromszög harmadik oldala {c}")










    