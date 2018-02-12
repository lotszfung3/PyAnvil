class Vector:
	'''
	force,acceleration,velocity in 2d mode
	possibly add: point of exertion
	'''
	def __init__(self,*coor):
		if(len(coor)==2):
			self.x=coor[0]
			self.y=coor[1]
		elif(len(coor)==1):
			self.x=coor[0][0]
			self.y=coor[0][1]
		else:
			raise Exception("{} doesn't match the arugments of vector.".format(coor))
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
	def __neg__(self):
		return Vector(-self.x,-self.y)

class Force(Vector):
	def __init__(self,x,y,id):
		super().__init__(x,y)
		self.id=id
	def __str__(self):
		return "id: {} ({}, {})".format(self.id,self.x,self.y)
