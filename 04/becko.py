rc = ("896010/4142")
cast1 = rc[:6]
cast2 = rc[7:]
cislo = cast1 + cast2
i = int(cislo)
if i % 11 == 0:
	print("True")
else:
	print("False")

