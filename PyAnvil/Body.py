from .Vector import Vector,Force
import numpy as np

class Body:
	'''
	Wall,ground
	'''
	def __init__(self,loc,dim,rotate=0,id="wa11"):
		self.loc=Vector(loc)
		self.dim=Vector(dim)
		self.movable=False
		self.id=id
		
		# clockwise rotation theta
		# Input in degree, stored in radians
		self.rotate= -rotate
	
	def get_coordinates(self):
		bodyCenter=np.array(self.loc.to_tuple())
		bodyDim=self.dim
		theta = self.rotate
		sin, cos = np.sin, np.cos
		rotMatrix = np.array([[cos(theta), -sin(theta)],[sin(theta),cos(theta)]])

		ul_x, ul_y = rotMatrix.dot(np.array([-bodyDim.x/2, -bodyDim.y/2])) + bodyCenter
		ur_x, ur_y = rotMatrix.dot(np.array([bodyDim.x/2, -bodyDim.y/2])) + bodyCenter
		bl_x, bl_y = rotMatrix.dot(np.array([-bodyDim.x/2, bodyDim.y/2])) + bodyCenter
		br_x, br_y = rotMatrix.dot(np.array([bodyDim.x/2, bodyDim.y/2])) + bodyCenter
		if str(self)=="Fixed":
			return (ul_x,ul_y,ur_x,ur_y, br_x, br_y, bl_x, bl_y)
		else:
			return (ul_x,ul_y, br_x, br_y)
	
	def __str__(self):
		return "Fixed"
	def update_force(self,*args):
		pass
	def update_state(self,*args):
		pass
class MovingBody(Body):
	DEBUG=False
	Obj_id=0
	def __init__(self,mass,charge=0,init_vel=(0,0),enab_colli=False,loc=(0,0),theta=0,isPoint=True,id=None):
		if(not id):	
			id="body"+ str(MovingBody.Obj_id) 
			MovingBody.Obj_id+=1
		super().__init__(loc,(10,10),id=id)
		self.mass=mass
		self.charge=charge
		self.enabled_collision=enab_colli
		self._forces={}#forces to be computed every step
		self.acceleration=Vector(0,0)
		self.velocity=Vector(init_vel)
		self.movable=True


	def __str__(self):
		if not MovingBody.DEBUG:
			return str(self.id)+" "+str(self.loc)
		else:
			return str(self.id)+" "+str(self.loc)+", ".join(str(x) for x in self._forces)

	def update_force(self,force):
		self._forces[force.id] = force
		return
		
	def update_state(self,delta_time,dumping=0.995):
		'''
		update the state of itself according to the force list
		'''
		sum_force = Force(0,0,'')
		for f in self._forces.values():
			sum_force += f
		self.acceleration=sum_force/self.mass
		self.velocity+=self.acceleration * delta_time / 1000
		#self.velocity*=dumping
		self.loc+=self.velocity* delta_time /1000
		#print(self.loc)
	def get_res_force(self):
		res_Force=Force(0,0,"")
		for i in self._forces.values():
			res_Force+=i
		return res_Force