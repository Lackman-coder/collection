a = int(input("Enter The First No: "))
b = int(input("Enter The Second No: "))
c = input("Enter the opreator +-///*: ")
result = 0
def calculation():
	
	if c == "+":
		 result=a+b
	elif c == "-":
		result = a-b
	elif c == "/":
		result = a/b
	elif c == "//":
		result = a//b
	elif c == "*":
		result = a*b
	else:
		print("opreator error choose only +-///*")
	
print("output:", a,c,b, "=", result)
calculation()
print("do u wanna calc again press y or n ")
def calcagain():
	g = input("y or n")
	if g == "y":
		calcagain.calculation()
	else:
		print("bye")
calcagain()