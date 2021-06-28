#using f string on oops class consturctor __init__(self)
print("1.oobs constuctor with fstring concept: \n")
class student:
	
	def __init__(self,name,std,subject,role):
		self.name = name
		self.std = std
		self.subject = subject
		self.role = role

lackman = student("lacku",12,"programing",10)
print(f"his name {lackman.name} he studied at {lackman.std} and he took subject is {lackman.subject} and his role on class {lackman.role} \n ")

#using fstring on normal variable assigning method 
print("2.normal variable assigning fstring concept: \n")
a = "lackman"
b = 28

print(f"his name is {a} and his age is {b}")