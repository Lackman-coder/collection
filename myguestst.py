i = 1
while i <= 7:
	a = int(input("guess thd no: "))
	if a < 18:
		print("you guess small")
	elif a > 18:
		print("you guess large")
	else:
		print("you win")
		print(7-i,"this much count you take to win")
		break
	i = i +1
	print(7- i,"you have this left")
if i > 7:
	print("game over")