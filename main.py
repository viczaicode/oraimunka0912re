#import egesznevesfeladat
#import neveseletkorosfeladat
#import szamosfeladat1
#import koratmerosfeladat
#import metodusok
import szovegkezeles

#*************************#
#                         #
#*** SZAMTANI FELADATOK***#
#                         #
#*************************#


#*** 1.,2. FELADAT ***#

#metodusok.feladat_1_2()


#*** 3., 4. FELADAT ***#

#metodusok.feladat_3_4()


#*** 5. FELADAT ***#

#atmero = metodusok.feladat_5()
#metodusok.keruletszamitas(atmero)
#terulet = metodusok.teruletszamitas(atmero)
#metodusok.korvegeredmeny(atmero, terulet)



#*** 6. FELADAT ***#

#a,b = metodusok.feladat_6()
#kerulet = metodusok.keruletszamitas2(a,b)
#terulet = metodusok.teruletszamitas2(a,b)
#metodusok.teglalaperedmeny(kerulet,terulet)



#*** 7. FELADAT ***#

#szam1,szam2,szam3 = metodusok.feladat_7()
#atlag = metodusok.mertaniszamolas(szam1,szam2,szam3)
#metodusok.mertanieredmeny(atlag)



#*** 8. FELADAT ***#

#a,b = metodusok.feladat8()
#c = metodusok.haromszogszamolas(a,b)
#metodusok.haromszogeredmeny(c)



#********************#
#                    #
#**  SZÖVEGKEZELÉS **#
#                    #
#********************#

#*** 1. FELADAT ***#

#nev = szovegkezeles.feladat_1()
#szovegkezeles.nevkiiras(nev)


#*** 2. FELADAT ***#

#nev = szovegkezeles.feladat_2()
#szovegkezeles.elsoharomkiiras(nev)


#*** 3. FELADAT ***#

#nev,vanabetu = szovegkezeles.feladat_3()
#szovegkezeles.vaneabetukiiras(vanabetu)


#*** 4.,5.,6.,7.,8.,9.,10 FELADAT ***#

nev = szovegkezeles.feladat_4_5_6_7_8_9_10()
vezeteknev = szovegkezeles.vezeteknev(nev)
keresztnev = szovegkezeles.keresztnev(nev)
szovegkezeles.vezeteknevkiiras(vezeteknev)
szovegkezeles.keresztnevkiiras(keresztnev)
szovegkezeles.nevkulonbsorbankiiras(vezeteknev,keresztnev)
szovegkezeles.hanykaraktervezeteknev(vezeteknev)
szovegkezeles.hanykarakterkeresztnev(keresztnev)
acsereere = szovegkezeles.abetucsereere(nev)
obetucsereora =szovegkezeles.obetucserenagyora(nev)
szovegkezeles.csereltbetukkiirasa(obetucsereora, acsereere)



