# *args methods:
	
def name(*args):
	name(a)
print("denser","anitha","lackman","drikas","rakshana" "\n")

def animal(*bets):
	animal(b)
print("cat","dog","parrot","fish" "\n")

def item(*home):
	for items in home:
		print(items)
		
item("tv","fridge","ac","electronics" "\n")

#if u not using *args then u cannot give moore arguments on function call example below:
'''
def frd(a,b,c):
	print(a,b,c)
	
frd("frd1","frd2","frd3","frd4")''' 
#uncmd above code and check error.

# **kwargs method:
	
def data(**kwargs):
	for key , value in kwargs.items():
		print("{} is {}".format (key,value))
data(name = "lackman", age=28, gender = "male", occupation = "seaman")