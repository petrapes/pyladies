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
    if pozice < 0:
      print("zaporna policka nejsou")
    elif pozice > 19:
      print("to je moc")
    elif pole[pozice] != "-":
      print("tam uz to nejde")
    else:
      pole = pole[:pozice] + "o" + pole[pozice+1:]
      return pole

def tah_pocitace(pole):
    # definuje tah pocitace
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
    print(tah_hrace(pole))
    pole = tah_hrace(pole)
    print(tah_pocitace(pole))
    pole = tah_pocitace(pole)
    print(vyhodnot(pole))
    vysledek = vyhodnot(pole)
    while True:
        if "-" in vysledek:
          print(tah_hrace(pole))
          pole = tah_hrace(pole)
          print(tah_pocitace(pole))
          pole = tah_pocitace(pole)
          print(vyhodnot(pole))
          vysledek = vyhodnot(pole)
        else:
          break
    print(pole)
    print("Game over")

piskvorky1d()