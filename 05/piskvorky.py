def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" in pole:
        return "-"
    else:
        return "!"

def tah_hrace(pole, cislo_policka):
    # Vrati herni pole s danym symbolem umistenym na danou pozici
    if cislo_policka not in range(0, 19) or pole[cislo_policka] == "x" or pole[cislo_policka] == "o":
        print("Zadej pozici v rozsahu 1-20, ktera neni obsazena")
        cislo_policka = int(input("Zadej cislo policka: "))
        return tah_hrace(pole, cislo_policka)
    else:
        pole = pole[:cislo_policka] + "o" + pole[cislo_policka+1:]
        return pole

def tah_pocitace(pole):
    # Vrati herni pole se zaznamenanym tahem pocitace
    import random
    policko = random.randint(0,19)
    if (pole[policko] != "x") or (pole[policko] != "o"):
        pole = pole[:policko] + "x" + pole[policko+1:]
        return pole
    else: 
        return tah_pocitace(pole)
     

def piskvorky1d():
    pole = "--------------------"
    print(pole)
    cislo_policka = int(input("Zadej cislo policka: "))
    print(tah_hrace(pole, cislo_policka))
    pole = tah_hrace(pole, cislo_policka)
    print(tah_pocitace(pole))
    pole = tah_pocitace(pole)
    print(vyhodnot(pole))
    vysledek = vyhodnot(pole)
    while "-" in vysledek:
        cislo_policka = int(input("Zadej cislo policka: "))
        print(tah_hrace(pole, cislo_policka))
        pole = tah_hrace(pole, cislo_policka)
        print(tah_pocitace(pole))
        pole = tah_pocitace(pole)
        print(vyhodnot(pole))
        vysledek = vyhodnot(pole)
    print(pole)
    print("Game over")

piskvorky1d()