class Vector:
	'''
	force,acceleration,velocity in 2d mode
	possibly add: point of exertion
	'''
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return "({}, {})".format(self.x,self.y)
	def __add__(self,other):
		if(isinstance(other,Vector)):
			return Vector(self.x+other.x,self.y+other.y)
		else:
			return Vector(self.x+other,self.y+other)
	def __mul__(self,other):
		if(isinstance(other,Vector)):
			return Vector(self.x*other.x,self.y*other.y)
		else:
			return Vector(self.x*other,self.y*other)
	def __truediv__(self,other):
		if(isinstance(other,Vector)):
			return Vector(self.x/other.x,self.y/other.y)
		else:
			return Vector(self.x/other,self.y/other)


class Force(Vector):
	def __init__(self,x,y,id):
		super().__init__(x,y)
		self.id=id
	def __str__(self):
		return "id: {} ({}, {})".format(self.id,self.x,self.y)
