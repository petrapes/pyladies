rc = input("zadej rodne cislo:")
cast1 = rc[0:6]
cast2 = rc[6]
cast3 = rc[7:11]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
odpoved = 0

cast12 = list(cast1)
for _ in cast12:
	if _ in numbers:
		odpoved = odpoved + 1
	else:
		False

if cast2 == "/":
	odpoved = odpoved + 1
else:
	False

cast32 = list(cast3)
for _ in cast32:
	if _ in numbers:
		odpoved = odpoved + 1
	else:
		False

if odpoved == 11:
	print("Spravne")
else:
	print("Spatne")