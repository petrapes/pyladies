from math import pi

def obsah_elipsy(a, b):
	"Vrati obsah elipsy"
	return 2 * pi * a * b

zaklad = obsah_elipsy(2, 3)

def valec(zaklad, v):
	return zaklad * v

print(valec(zaklad, 4))


