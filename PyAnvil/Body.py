from .Vector import Vector
class Body:
	def __init__(self,id,mass=10,group_id=0):	
		self.id=id
		self.group_id=group_id
		self.mass=mass
		self.loc=Vector(300,300)
		self._velocity=Vector(0,0)
		self._prev_velocity=Vector(0,0)
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
	@property
	def velocity(self):
		return self._velocity
	@velocity.setter
	def velocity(self,new_vel):
			self._velocity=new_vel / (self.mass) * 20
	def compute_loc(self):
			self.loc+=self._velocity
			self._prev_velocity=self._velocity
			self._velocity=0

class GroupBody(Body):
	'''
	the body imitating 
	'''
	def __init__(self,id,mass=100):
		super().__init__(self,id)