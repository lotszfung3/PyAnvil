from .Vector import Vector
class Body:
	Obj_id=0
	def __init__(self,mass=10):	
		self.id=Body.Obj_id 
		Body.Obj_id+=1
		self.mass=mass
		self.loc=Vector(300,300)
		self.velocity=Vector(0,0)
	def __eq__(self,other):
		return self.id==other.id
	def __str__(self):
		return str(self.id)+" "+str(self.loc)
	def get_coordinates(self):
		return (self.loc.x-self.mass,self.loc.y-self.mass,
				self.loc.x+self.mass,self.loc.y+self.mass)
	def get_sq_distance(self,x,y):
		'''
		return the square distance of the center of this body with the arguments
		'''
		return (self.loc.x-x)**2+(self.loc.y-y)**2