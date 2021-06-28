class details:
	def dit(self):
		return f"he is {self.name} and he was {self.work} he did complete {self.std} "
	
	
lack = details()
lack.name = "lackman"
lack.work = "seaman"
lack.std = 12

print(lack.dit())