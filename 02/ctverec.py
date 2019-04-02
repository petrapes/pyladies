#poznamky jaky chcu
strana = float(input("Zadej cislo"))
cislo_je_spravne = strana > 0
print(cislo_je_spravne)
if cislo_je_spravne:
	print("obvod čtverce se stranou", strana, "je", 4 * strana, "cm")
	print("obsah čtverce se stranou", strana, "je", strana * strana, "cm2")
else:
	print("zadej kladne cislo")
print("dekujeme za navstevu")