


# Teretulemast, kui seda loed, siis oled minu koodilõigu leidnud GitHubist.
# Selgitus EV isikukoodile põhjal on kirjutatud see kood. / http://www.cs.tlu.ee/~inga/progbaas/Praktiline/isikukood.txt - kasutatud materjal.
# Minu koduleht on https://www.nigol.me / Projekt on tehtud puhtalt huvi pärast info- ja kommunikatsioonitehnoloogia eriala õppiva õpilase Rait Nigoli poolt.
# decoder v1.0.0 by Rait Nigol

def main():
    # Importime funktsiooni(d)
    import time

    # Defineerime mõned muutujad
    n = "naine"
    m = "mees"
    a18 = "1800-1899"
    a19 = "1900-1999"
    a20 = "2000-2099"

    # Veateated hoitakse siin
    errorx011 = "Oih! Nüüd läks küll midagi viltu! Isikukood peab olema 11 tähemärki pikk! Alustame otsast peale."
    error = "Vabandust, aga midagi läks valesti! Kas sisestasite korrektse isikukoodi? Alustame otsast peale."

    # Väljutame informatsiooni koodi kohta.
    print("Tere! Kasutate isikukoodi lahtimurdjat (v1.0.0)."); time.sleep(1); print("Kood on loodud Nigol Enterprises © (https://www.nigol.me) poolt."); time.sleep(1)

    # Käsime kasutajal isikukood sisestada.
    isikukood = input("Palun sisestage oma isikukood: ")
    e_arv = isikukood[0:1]

    # Kui isikukood ei ole 11 tähemärki pikk, visatakse kasutaja algusesse tagasi.
    if len(isikukood) is not 11:
        print(errorx011); time.sleep(2); main()

    # Võtame isikukoodi esimese arvu ning see annab meile vastuseks, mis ajaperioodil antud inimene sündinud on.
    if isikukood[0:1] < "1" or isikukood[0:1]> "6":
        print(error); time.sleep(2); main()

    # Kui isikukood algab numbriga 1, 2, 3, 4, 5 või 6, lubatakse järgnevad käsud. Vastasel juhul suunatakse teid algusesse tagasi.
    if isikukood[0:1] == "1" or "2" or "3" or "4" or "5" or "6":
        time.sleep(1)
        print("Genereerin tulemusi...")
        time.sleep(1)
        if e_arv == "1":
            print("Te olete aastail " + a18 + " " + "sündinud " + m); saAlgus = "18"; sugu = "mees"
        if e_arv == "2":
            print("Te olete aastail " + a18 + " " + "sündinud " + n); saAlgus = "18"; sugu = "naine"
        if e_arv == "3":
            print("Te olete aastail " + a19 + " " + "sündinud " + m); saAlgus = "19"; sugu = "mees"
        if e_arv == "4":
            print("Te olete aastail " + a19 + " " + "sündinud " + n); saAlgus = "19"; sugu = "naine"
        if e_arv == "5":
            print("Te olete aastail " + a20 + " " + "sündinud " + m); saAlgus = "20"; sugu = "mees"
        if e_arv == "6":
            print("Te olete aastail " + a20 + " " + "sündinud " + n); saAlgus = "20"; sugu = "naine"
    time.sleep(1); print("============================================"); time.sleep(1)

    # Defineerime muutujad, mis aitavad meil kuvada sünnipäeva, soo, järjekorranumbri kui ka kontrollnumbri.
    saLopp = isikukood[1:3]; sAasta = saAlgus + saLopp
    skPaev = isikukood[5:7]
    skNumber = isikukood[3:5]
    synnipaev = skPaev + "/" + skNumber + "/" + sAasta
    jarjekorranumber = isikukood[7:10]
    kontrollnumber = isikukood[10]

    # Väljutame tulemuse
    print("        Te olete sündinud " + synnipaev); time.sleep(1)
    print("        Teie sooks on          " + sugu); time.sleep(1)
    print("        Teie järjekorranumber on " + jarjekorranumber); time.sleep(1)
    print("        Teie kontrollnumber on     " + kontrollnumber); time.sleep(1)
    print("============================================"); time.sleep(2)

    # Laseme kasutajal valida, kas ta soovib otsast peale alustada või programmi sulgeda.
    restart = input("Kas soovite uuesti peale alustada (JAH/EI)?: ").lower()
    if restart == "jah":
        main()
    else:
        exit()
main()