def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" in pole:
        return "-"
    else:
        return "!"

def tah_hrace(pole):
    # zkontroluje, ze tah hrace dava smysl
    pozice = int(input("Zadej cislo policka:"))
    while True:
        if pozice < 0:
            print("zaporna policka nejsou")
            return tah_hrace(pole)
        elif pozice > 19:
            print("to je moc")
            return tah_hrace(pole)
        elif pole[pozice] != "-":
            print("tam uz to nejde")
            return tah_hrace(pole)
        else:
            pole = pole[:pozice] + "o" + pole[pozice+1:]
            return pole

def tah_pocitace(pole):
    # definuje tah pocitace
    import random
    policko = random.randint(0,19)
    while True: 
        if pole[policko] == "-":
            pole = pole[:policko] + "x" + pole[policko+1:]
            return pole
        else:
            break
    return pole

def piskvorky1d():
    pole = "--------------------"
    print(pole)
    while True:
        pole = tah_hrace(pole)
        print(pole)
        pole = tah_pocitace(pole)
        print(pole)
        if vyhodnot(pole) != "-":
            break
    print(pole)
    print("Vyhral", vyhodnot(pole))

piskvorky1d()
