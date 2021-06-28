while True:
	try:
		a = int(input("enter the 1 value: "))
		b = int(input("enter the 2 value: "))
		c = input("select oprt */+-: ")
		if c == "+":
			result = a+b
			print("output: ",a,c,b,"=",result)
			print("do u want calc again")
			d = input("y or n: ")
			if d != "y":
				break
		else:
			c != "+*/-"
			print("oprt error")
	except:
		continue