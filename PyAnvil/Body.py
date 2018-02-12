from .Vector import Vector,Force

class Body:
	'''
	Wall,ground
	'''
	def __init__(self,loc,dim):
		self.loc=Vector(loc)
		self.dim=Vector(dim)
		self.movable=False
	def __str__(self):
		return "Fixed"
	def update_force(self,*args):
		raise Exception("Wall should have no force")
	def update_state(self,*args):
		raise Exception("It state won't change")
class MovingBody(Body):
	DEBUG=False
	Obj_id=0
	def __init__(self,mass,charge=0,init_vel=(0,0),enab_colli=False,loc=(0,0),theta=0,isPoint=True,id=None):
		super().__init__(loc,(5,5))
		self.mass=mass
		self.charge=charge
		self.enabled_collision=enab_colli
		self._forces=[]#forces to be computed every step
		self.acceleration=Vector(0,0)
		self.velocity=Vector(init_vel)
		self.movable=True
		if(not id):	
			self.id="body"+ str(MovingBody.Obj_id) 
			MovingBody.Obj_id+=1
		else:
			self.id=id

	def __str__(self):
		if not MovingBody.DEBUG:
			return str(self.id)+" "+str(self.loc)
		else:
			return str(self.id)+" "+str(self.loc)+", ".join(str(x) for x in self._forces)

	def update_force(self,force):
		for f in self._forces:
			if(f.id==force.id):
				f.x=force.x
				f.y=force.y
				return
		self._forces.append(force)
	def update_state(self,delta_time):
		'''
		update the state of itself according to the force list
		'''
		sum_force=sum(self._forces,Force(0,0,""))
		self.acceleration=sum_force/self.mass
		self.velocity+=self.acceleration * delta_time / 1000
		self.loc+=self.velocity* delta_time /1000
		#print(self.loc)
