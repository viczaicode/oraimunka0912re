def feladat_1():
    nev:str = str.upper(input("Kérlek add meg a neved: "))
    return nev

def nevkiiras(nev):
    print(nev)

def feladat_2():
    nev:str = str(input("Kérlek add meg a neved: "))
    return nev

def elsoharomkiiras(nev):
    print(nev[0])
    print(nev[1])
    print(nev[2])

def feladat_3():
    nev:str = str(input("Kérlek add meg a neved: "))
    vanabetu = nev.find("a")
    return nev,vanabetu

def vaneabetukiiras(vanabetu):
    print(vanabetu)

def feladat_4_5_6_7_8_9_10():
    nev:str = str(input("Kérlek add meg a teljes neved: "))
    return nev

def vezeteknev(nev):
    szokoz:str = nev.find(" ")
    vezeteknev:str = (nev[0:szokoz])
    return vezeteknev

def keresztnev(nev):
    szokoz:str = nev.find(" ")
    utolsoindex = len(nev)
    keresztnev:str = (nev[szokoz+1:utolsoindex])
    return keresztnev

def vezeteknevkiiras(vezeteknev):
    print(f"Vezetékneved: {vezeteknev}")

def keresztnevkiiras(keresztnev):
    print(f"Keresztneved: {keresztnev}")

def nevkulonbsorbankiiras(vezeteknev,keresztnev):
    print(f"Külön sorban a vezetékneved: {vezeteknev}")
    print(f"Külön sorban a keresztneved: {keresztnev}")

def hanykaraktervezeteknev(vezeteknev):
    print(f"Ennyi karakterből áll a vezetékneved: {len(vezeteknev)-1}")

def hanykarakterkeresztnev(keresztnev):
    print(f"Ennyi karakterből áll a keresztneved: {len(keresztnev)-1}")

def abetucsereere(nev):
    utolsoindex = len(nev)
    abetumegtalalasa = nev.find("a")
    print(f"Az első a betű ezen az indexen van: {abetumegtalalasa}")
    acsereere = nev.replace("a", "e")
    return acsereere

def obetucserenagyora(nev):
    obetucsereora = nev.replace("o", "O")
    return obetucsereora

def csereltbetukkiirasa(obetucsereora, acsereere):
    print(f"A módosított neved úgy, hogy a kis o betűk ki lettek cserélve nagy O betűre: {obetucsereora}")
    print(f"A módosított neved úgy, hogy a a betűk ki lettek cserélve e betűre: {acsereere}")
