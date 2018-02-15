from math import sqrt
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
	def normalize(self,mag):
		#normalize to magnitude 
		if(self.x==0 and self.y==0):
			return
		if(self.x==0):
			self.y=mag * (-1 if  self.y<0 else 1)
		elif self.y==0:
			self.x=mag * (-1 if  self.x<0 else 1)
		else:
			sq_rt=sqrt(self.x**2+self.y**2)
			self.x=mag*self.x/sq_rt
			self.y=mag*self.y/sq_rt
	def sq_magnitude(self):
		return self.x**2+self.y**2
	def projection_in(self,b):
		b_sq_magt=b.sq_magnitude()
		res_force=b *  ((self.x*b.x+self.y+b.y)/b_sq_magt )
		return Vector(res_force.x,res_force.y)
	def perpedicular_in(self,b):
		b_sq_magt=b.sq_magnitude()
		res_force=self-  b * ((self.x*b.x+self.y+b.y)/b_sq_magt )
		return Vector(res_force.x,res_force.y)
class Force(Vector):
	def __init__(self,*args):
		assert(len(args)==3)
		super().__init__(args[0],args[1])
		self.id=args[2]
	def __str__(self):
		return "id: {} ({}, {})".format(self.id,self.x,self.y)
	def __add__(self,other):
		if(isinstance(other,Vector)):
			return Force(self.x+other.x,self.y+other.y,self.id)
		else:
			return Force(self.x+other,self.y+other,self.id)
	def __sub__(self,other):
		if(isinstance(other,Vector)):
			return Force(self.x-other.x,self.y-other.y,self.id)
		else:
			return Force(self.x-other,self.y-other,self.id)
	def __mul__(self,other):
		if(isinstance(other,Vector)):
			return Force(self.x*other.x,self.y*other.y,self.id)
		else:
			return Force(self.x*other,self.y*other,self.id)
	def __truediv__(self,other):
		if(isinstance(other,Vector)):
			return Force(self.x/other.x,self.y/other.y,self.id)
		else:
			return Force(self.x/other,self.y/other,self.id)
	def __neg__(self):
		return Force(-self.x,-self.y,self.id)
	def projection_in(self,b):
		b_sq_magt=b.sq_magnitude()
		res_force=b *  ((self.x*b.x+self.y+b.y)/b_sq_magt )
		return Force(res_force.x,res_force.y,self.id)
	def perpedicular_in(self,b):
		b_sq_magt=b.sq_magnitude()
		res_force=self-  b * ((self.x*b.x+self.y+b.y)/b_sq_magt )
		return Force(res_force.x,res_force.y,self.id)
	