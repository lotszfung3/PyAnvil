from math import sqrt

class Vector:
	_turn=0
	def __init__(self,*args):
		self.x=args[0]
		self.y=args[1]
	def __str__(self):
		return "({}, {})".format(self.id,self.x)
	def __add__(self,other):
		if(isinstance(other,Vector)):
			return Vector(self.x+other.x,self.y+other.y)
		else:
			return Vector(self.x+other,self.y+other)
	def __sub__(self,other):
		if(isinstance(other,Vector)):
			return Vector(self.x-other.x,self.y-other.y)
		else:
			return Vector(self.x-other,self.y-other)
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
	def sq_magn(self):
		return self.x**2 + self.y**2
	def to_magn(self,magn):
		self_magn=self.sq_magn()**0.5
		return Vector(self.x/self_magn,self.y/self_magn)
	def get_a_vector():
		Vector._turn=Vector._turn%17+1
		return Vector(Vector._turn * 11.08 % 1,Vector._turn * 30.09 % 1)