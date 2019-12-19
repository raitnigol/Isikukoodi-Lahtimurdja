ID = input("Palun sisestage oma isikukood: ")


def getiddata(isikukood):
    if len(isikukood) is not 11:
        raise ValueError("Oih! Nüüd läks küll midagi viltu! Isikukood peab olema 11 tähemärki pikk!")
    e_arv = isikukood[0:1]
    if e_arv < "1" or e_arv > "6":
        raise ValueError("Vabandust, aga midagi läks valesti! Kas sisestasite korrektse isikukoodi?")

    global sugu
    global saLopp
    global skPaev
    global skNumber
    global jarjekorranumber
    global kontrollnumber
    global synnipaev
    global andmed

    if e_arv == "1" or e_arv == "3" or e_arv == "5":
        sugu = "mees"
    if e_arv == "2" or e_arv == "4" or e_arv == "6":
        sugu = "naine"

    saLopp = isikukood[1:3]
    skPaev = isikukood[5:7]
    skNumber = isikukood[3:5]
    jarjekorranumber = isikukood[7:10]
    kontrollnumber = isikukood[10]

    if e_arv == "1" or e_arv == "2":
        synnipaev = skPaev + "/" + skNumber + "/" + "18" + saLopp
    if e_arv == "3" or e_arv == "4":
        synnipaev = skPaev + "/" + skNumber + "/" + "19" + saLopp
    if e_arv == "5" or e_arv == "6":
        synnipaev = skPaev + "/" + skNumber + "/" + "20" + saLopp


getiddata(ID)


# Väljutame tulemuse
print("============================================")
print("Sündinud                 " + synnipaev)
print("Sugu                     " + sugu)
print("Teie järjekorranumber on " + jarjekorranumber)
print("Teie kontrollnumber on   " + kontrollnumber)
print("=============================================")
