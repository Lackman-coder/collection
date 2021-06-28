class employee:
	def __init__(self,aname,aoccu,astd,awork):
		self.name = aname
		self.occu = aoccu
		self.std = astd
		self.work = awork
	
lackman=employee("lacku","selfemployer",12,"seaman")
print(lackman.name)