from datetime import date
kordajad1 = [1,2,3,4,5,6,7,8,9,1]
kordajad2 = [3,4,5,6,7,8,9,1,2,3]
ID = input('Isikukood: ')

def validate_id(isikukood):
    global e_arv
    if len(isikukood) != 11:
        raise ValueError('Isikukood peab olema 11 tähemärki pikk!')
    e_arv = isikukood[0:1]
    if e_arv < '1' or e_arv > '6':
        raise ValueError('Sisestage korrektne isikukood (esimene number 1-6)')

ID_array = list(ID[0:11])
ID_control_array = list(ID[0:10])
for i in range(0, len(ID_array)):
    ID_array[i] = int(ID_array[i])
for i in range(0, len(ID_control_array)):
    ID_control_array[i] = int(ID_control_array[i])

ID_last_number = ID_array[10]
kontrollnumber_kokku = [a * b for a, b in zip(ID_array, kordajad1)]

kontrollnumber_jaak = sum(kontrollnumber_kokku) % 11

if kontrollnumber_jaak == 10:
if kontrollnumber_jaak != ID_last_number:
  raise ValueError('Isikukood ei ole kehtiv!')
if kontrollnumber_jaak == 10:
  multiplied = [a * b for a, b in zip(ID_array, kordajad2)]
  kontrollnumber_jaak = sum(kontrollnumber_kokku) % 11
  if kontrollnumber_jaak == 10:
    kontrollnumber_jaak = 0
    if kontrollnumber_jaak != ID_last_number:
      print(kontrollnumber_jaak, ID_last_number)
      raise ValueError('Isikukood ei ole kehtiv!')

def getiddata(isikukood):
    validate_id(isikukood)

    global sugu
    global saLopp
    global skPaev
    global skNumber
    global jarjekorranumber
    global kontrollnumber
    global synnipaev
    global prgAasta

    saLopp = isikukood[1:3]
    skPaev = isikukood[5:7]
    skNumber = isikukood[3:5]
    jarjekorranumber = isikukood[7:10]
    kontrollnumber = isikukood[10]

    if e_arv in ('1', '3', '5', '7'):
        sugu = 'Mees'
    if e_arv in ('2', '4', '6', '8'):
        sugu = 'Maine'

    if e_arv in ('1', '2'):
        synnipaev = skPaev + '/' + skNumber + '/' + '18' + saLopp
    if e_arv in ('3', '4'):
        synnipaev = skPaev + '/' + skNumber + '/' + '19' + saLopp
    if e_arv in ('5', '6'):
        synnipaev = skPaev + '/' + skNumber + '/' + '20' + saLopp
    if e_arv in ('7', '8'):
        synnipaev = skPaev + '/' + skNumber + '/' + '21' + saLopp
    # 30 päevaga kuud, kui isikukoodis skPaev on suurem kui 30, kood peatatakse.
    if skNumber in ('04', '06', '09', '11'):
        if skPaev > '30':
            raise ValueError('Sellel kuul ei ole rohkem kui 30 päeva!')

    # 31 päevaga kuud, kui isikukoodis skPaev on suurem kui 31, kood peatatakse.
    if skNumber in ('01', '03', '05', '07', '08', '10', '12'):
        if skPaev > '31':
            raise ValueError('Sellel kuul ei ole rohkem kui 31 päeva!')

    # Veebruaris on liigaastatel 1 päev rohkem, kui skPaev ei klapi, kood peatatakse.
    liigaasta(int(synnipaev[6:11]))
    if liigaasta is True:
        if skPaev > '29':
            raise ValueError('Sellel kuul ei ole rohkem kui 29 päeva!')
    if liigaasta is False:
        if skPaev > "28":
            raise ValueError('Sellel kuul ei ole rohkem kui 28 päeva!')

    # Inimene ei saa sündida tulevikus
    prgAasta = date.today().year

    if int(synnipaev[6:11]) > prgAasta:
        raise ValueError('Inimene ei saa sündida tulevikus')


def liigaasta(aasta):
    global liigaasta

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


getiddata(ID)

print('\n=== ISIKUKOODI ' + ID + ' ANDMED ===')
print('Sündinud         ' + synnipaev)
print('Sugu             ' + sugu)
print('Järjekorranumber ' + jarjekorranumber)
print('Kontrollnumber   ' + kontrollnumber)
print('=====================================')
