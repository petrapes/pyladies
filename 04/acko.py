rc = list("896010/4142")
numbers = ["0","1","2","3","4","5","6","7","8","9","/"]

for _ in rc:
	if _ in numbers and rc[6] == "/":
		print("True")
	else:
		print("False")
