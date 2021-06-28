import random

choice = input("enter the password you want to make random: ")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
sympols = "&$()@#?!¥©¢£"

all = choice + upper + lower + numbers + sympols

length = 16

password = " " . join(random.sample(all , length))
print("your password is : " , password)