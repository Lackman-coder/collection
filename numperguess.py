a = 18
print("no guessing game\n")
print("no of guessing only 7 count you have\n")
count = 1
while (count <= 7):
	ask = int(input("enter your guessing: "))
	if ask > 18:
		print("you guessd bigger\n")
	elif ask < 18:
		print("you guessed smaller\n")
	else:
		print("you win")
		print(count,"count you took to win")
		break
	print("you have remain count: ", 7-count)
	count = count + 1
if (count > 7):
	print("game over")