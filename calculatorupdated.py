a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = input("enter your operator +-/* : ")
d = "wrong operator"

result = 0

if c == "+":
	result = (a + b)
elif c == "-":
	result = (a - b)
elif c == "*":
	result = (a * b)
elif c == "/":
	result = (a / b)
elif c != "+-*/":
	result = (d)

print("result : " , a, c, b, "=" ,result)