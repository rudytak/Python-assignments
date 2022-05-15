slovnik = {
    "K": 0,
    "X": -1,
    "_": -3,
    "C": -2
    }
    
def prepis_slovniku():
    slovnik2 = {}
    for klic, hodnota in slovnik.items():
        slovnik2[hodnota] = klic
    return slovnik2

slovnik2 = prepis_slovniku() 

def nacti_pole(slovnik):
    list_krizku = 12*[-1]
    pole = []
    for i in range(2):
        pole.append(list_krizku)
    with open("vstup.txt") as f:
        for radek in f.readlines():
            radky = 2*[-1]
            for znak in radek.strip():
                znak1 = slovnik[znak]
                radky.append(znak1)
            radky += 2*[-1]
            pole.append(radky)
    for i in range(2):
        pole.append(list_krizku)
    return pole

def najdi_kone(pole):
    for listik in pole:
        for znak in listik:
            if znak == 0:
                souradnice1 = pole.index(listik)
                souradnice2 = listik.index(znak)
    return souradnice1, souradnice2 

def najdi_vsechna(pole, hledana_hodnota):
    list_souradnic = []
    for listik in pole:
        for znak in listik:
            if znak == hledana_hodnota:
                list_souradnic.append ([pole.index(listik),listik.index(znak)])
    return list_souradnic
          
def napis_volna_mista_a_prepis(pole, souradnice1, souradnice2):
    nasli_jsme_C = False
    for i in range (-1,2,2):
        if pole[souradnice1 - 2][souradnice2 + i] == -2 :
            nasli_jsme_C = True
        if pole[souradnice1 - 2][souradnice2 + i] == -3 :
            pole[souradnice1 - 2][souradnice2 + i] = pole[souradnice1][souradnice2] + 1

        if pole[souradnice1 + 2][souradnice2 + i] == -2 :
            nasli_jsme_C = True
        if pole[souradnice1 + 2][souradnice2 + i] == -3 :
            pole[souradnice1 + 2][souradnice2 + i] = pole[souradnice1][souradnice2] + 1

        if pole[souradnice1 + i][souradnice2 - 2] == -2 :
            nasli_jsme_C = True
        if pole[souradnice1 + i][souradnice2 - 2] == -3 :
            pole[souradnice1 + i][souradnice2 - 2] = pole[souradnice1][souradnice2] + 1

        if pole[souradnice1 + i][souradnice2 + 2] == -2 :
            nasli_jsme_C = True
        if pole[souradnice1 + i][souradnice2 + 2] == -3 :
            pole[souradnice1 + i][souradnice2 + 2] = pole[souradnice1][souradnice2] + 1

    return pole, nasli_jsme_C

def vypis_pole(pole, slovnik2):
    for y in range(len(pole)):
        for x in range(len(pole[y])):
            try:
                znak = slovnik2[pole[y][x]]
                print(znak, end="")
            except:
                print(pole[y][x], end="")
                pass
        print()
    return pole

pole = nacti_pole(slovnik)

nasli_jsme = False
opakovani = 1
maximalni_opakovani = 100
pozice_ktere_zkoumat = [najdi_kone(pole)]
while not nasli_jsme:
    for pozice in pozice_ktere_zkoumat:
        pole, nasli_jsme = napis_volna_mista_a_prepis(pole, pozice[0], pozice[1])
        if nasli_jsme:
            print(opakovani)
            break

    dalsi_pozice_ktere_zkoumat = najdi_vsechna(pole, opakovani)
    pozice_ktere_zkoumat = dalsi_pozice_ktere_zkoumat

    opakovani+=1
    if opakovani > maximalni_opakovani:
        print("-1")
        break

#vypis_pole(pole, slovnik2)