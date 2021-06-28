def calculate():
	a = int(input("enter your first number: "))
	b = int(input("enter your second number: "))
	c = input("enter your operator +-/* : ")
	d = "wrong operator"
	
	if c == "+":
		print('{} + {} =' .format(a , b),(a + b))
	elif c == "-":
		print('{} - {} =' .format(a , b),(a - b))
	elif c == "*":
		print('{} * {} =' .format(a , b),(a * b))
	elif c == "/":
		print('{} / {} =' .format(a , b),(a / b))
	else:
		print("you entered wrong operator")
		
	again()
def again():
	p = input("do u want calculate again enter y means yes n means no?")
	if p.upper() == "Y":
		calculate()
	elif p.upper() == "N":
		print("good bye")
	else:
		again()
		
calculate()