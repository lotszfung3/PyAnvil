from .Vector import Vector,Force


class Body:
	DEBUG=False
	Obj_id=0
	def __init__(self,mass,charge=0,init_vel=Vector(0,0),enab_colli=False,loc=Vector(0,0),theta=0,isPoint=True):
		self.id="body"+str(Body.Obj_id)
		Body.Obj_id+=1
		self.mass=mass
		self.charge=charge
		self.enabled_collision=enab_colli
		self.loc=loc
		self._forces=[]#forces to be computed every step
		self.acceleration=Vector(0,0)
		self.velocity=init_vel

	def __str__(self):
		if not Body.DEBUG:
			return str(self.id)+" "+str(self.loc)
		else:
			return str(self.id)+" "+str(self.loc)+", ".join(str(x) for x in self._forces)

	def add_force(self,force):
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



