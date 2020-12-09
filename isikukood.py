# Isikukoodi valideerimise jaoks tehtud skript. skript võtab kasutajalt isikukoodi,
# ja väljastab kasutajale andmed selle kohta. (sünnikuupäev, sugu) jne.

# Kõigepealt importime mooduli datetime, sellest funktsiooni date
from datetime import date

# ID-kaardi kordajad
kordajad1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,1]
kordajad2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

# Küsime kasutajalt ID-koodi

ID = input('Isikukood: ')

# Funktsioon, et valideerida ID-kood
def valideeri_id(isikukood):
    # Kas isikukood on 11 tähemärki
    if len(isikukood) != 11:
        raise ValueError('Isikukood peab olema täpselt 11 tähemärki pikk!')
    # ID-koodi esimene arv soo ja sünni määramiseks
    id_esimene_arv = isikukood[0:1]
    if id_esimene_arv < '1' or id_esimene_arv > '6':
        raise ValueError('Sisestage korrektne isikukood (esimene number peab jääma vahemikku 1 kuni 6)')
    return id_esimene_arv

# Muudame id koodi kõik väärtused järjendiks, et korrutada läbi kordajatega
ID_järjend = list(ID[0:11])
ID_kontrolljärjend = list(ID[0:10])

for i in range(0, len(ID_järjend)):
    ID_järjend[i] = int(ID_järjend[i])
for i in range(0, len(ID_kontrolljärjend)):
    ID_kontrolljärjend[i] = int(ID_kontrolljärjend[i])
    
# Arvutame kontrollnumbri
ID_viimane_number = ID_järjend[10]

kontrollnumber_kokku = [a * b for a, b in zip(ID_järjend, kordajad1)]
kontrollnumber_jääk = sum(kontrollnumber_kokku) % 11
if kontrollnumber_jääk == 10:
    kontrollnumber_jääk = 0
    if kontrollnumber_jääk != ID_viimane_number:
        raise ValueError('Isikukood ei ole kehtiv!')
    else:
        korrutatud = [a * b for a, b in zip(ID_järjend, kordajad2)]
        kontrollnumber_jääk = sum(kontrollnumber_kokku) % 11
        if kontrollnumber_jääk == 10:
            kontrollnumber_jääk = 0
            if kontrollnumber_jääk != ID_viimane_number:
                raise ValueError('Isikukood ei ole kehtiv!')

# Saame isikukoodist andmed
def isikukoodi_andmed(isikukood):
    id_esimene_arv = valideeri_id(isikukood)
    
    # defineerime muutujad
    global sugu
    global sünniaasta_lõpp
    global sünnikuupäev
    global sünnikuunumber
    global järjekorranumber
    global kontrollnumber
    global sünnipäev
    global praegune_aasta
    
    sünniaasta_lõpp = isikukood[1:3]
    sünnikuupäev = isikukood[5:7]
    sünnikuunumber = isikukood[3:5]
    järjekorranumber = isikukood[7:10]
    kontrollnumber = isikukood[10]
    
    # Kontrollime kas isik on mees või naine
    if id_esimene_arv in ('1', '3', '5', '7'):
        sugu = 'Mees'
    elif id_esimene_arv in ('2', '4', '6', '8'):
        sugu = 'Naine'
        
    # Sünniaasta saamine
    if id_esimene_arv in ('1', '2'):
        sünnipäev = sünnikuupäev + '/' + sünnikuunumber + '/' + '18' + sünniaasta_lõpp
    elif id_esimene_arv in ('3', '4'):
        sünnipäev = sünnikuupäev + '/' + sünnikuunumber + '/' + '19' + sünniaasta_lõpp
    elif id_esimene_arv in ('5', '6'):
        sünnipäev = sünnikuupäev + '/' + sünnikuunumber + '/' + '20' + sünniaasta_lõpp
    elif id_esimene_arv in ('7', '8'):
        sünnipäev = sünnikuupäev + '/' + sünnikuunumber + '/' + '21' + sünniaasta_lõpp 
    
    # 30 päevaga kuud, kui isikukoodis sünnikuupäev on suurem kui 30, siis kood peatatakse
    if sünnikuunumber in ('04', '06', '09', '11'):
        if sünnikuupäev > '30':
            raise ValueError('Sellel kuul ei ole rohkem kui 30 päeva!')
    # 31 päevaga kuud, kui isikukoodis sünnikuupäev on suurem kui 31, siis kood peatatakse
    if sünnikuunumber in ('01', '03', '05', '07', '08', '10', '12'):
        if sünnikuupäev > '31':
            raise ValueError('Sellel kuul ei ole rohkem kui 31 päeva!')
        
    # Kuna veebruaris on liigaastatel 1 päev rohkem, peab vaatama, kas sünnikuupäev klapib
    liigaasta(int(sünnipäev[6:11]))
    if liigaasta is True:
        if sünnikuupäev > '29':
            raise ValueError('Sellel kuul ei ole rohkem kui 29 päeva!')
    elif liigaasta is False:
        if sünnikuupäev > '28':
            raise ValueError('Sellel kuul ei ole rohkem kui 28 päeva!')

    # Kuna inimene ei saa sündida tulevikus, siis kontrolli, kas sünnipäev on praegusest ajast kaugemal
    praegune_aasta = date.today().year
    
    if int(sünnipäev[6:11]) > praegune_aasta:
           raise ValueError('Inimene ei saa sündida tulevikus!')

# Kontrollime, kas aasta on liigaasta või mitte
def liigaasta(aasta):
    if (aasta % 4) == 0:
        if (aasta % 100) == 0:
            if (aasta % 400) == 0:
                liigaasta = True
            else:
                liigaasta = False
        else:
                liigaasta = True
    else:
            liigaasta = False
    return liigaasta

# Saame isikukoodi kohta andmed
isikukoodi_andmed(ID)

# Väljastame andmed
print('\n=================================')
print('ISIKUKOODI   ' + ID + '   ANDMED')
print('Sugu: ' + sugu)
print('\tSÜNNIAEG: ')
print('\tAasta: ' + sünnipäev[6:11])
print('\tKuu: ' + sünnipäev[4:5])
print('\tPäev: ' + sünnipäev[0:2])
print('=================================')
