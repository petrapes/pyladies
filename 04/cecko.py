rc = ("896010/4142")
den1 = rc[4:6]
mesic1 = rc[2:4]
rok1 = "19" + rc[0:2]

den2 = int(den1)
mesic2 = int(mesic1)
rok2 = int(rok1)

if mesic2 > 12:
	mesic2 = (mesic2 - 50)
else:
	mesic2

if rok2 < 18:
	rok2 = "20" + rc[0:2]
else:
	rok2

print(den2, mesic2, rok2)
