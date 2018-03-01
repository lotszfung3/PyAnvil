from .Body import Body
from .Vector import Vector
from typing import List
from time import sleep

class Space:
	'''
	The whole world
	'''
	def __init__(self,bodyList=[],delta_time=30):
		self.bodyList=bodyList
		self.force_list=[]
		self.delta_time=delta_time
	def __str__(self):
		bodyStr="Bodies:\n"+"\n".join(str(x) for x in self.bodyList) if len(self.bodyList)>0 else "No objects"
		return bodyStr
	def compute_force(self,rate):
		pass
	def compute_collide(self):
		'''
		avoiding the overlapping of bodies
		time complexity of O(n**2) now, should be able to reduce it by sorting
		the bodies in x or y
		'''
		for a in self.bodyList:
			for b in self.bodyList:
				if (a!=b):
					loc_diff=b.loc-a.loc
					if(loc_diff.x==0 and loc_diff.y==0):
						loc_diff=Vector.get_a_vector()
					if (loc_diff.sq_magn()<=(a.mass+b.mass)**2):
						b.velocity=loc_diff.to_magn(1)
						a.velocity=-loc_diff.to_magn(1)
					
	def compute_vel(self,rate):
		for b in self.bodyList:
			b.loc+=b.velocity
			b.velocity=0
	def step(self,period=None):
		'''
		Get the space after period ms
		input:
			period:
		'''		
		self.compute_force(self.delta_time if not period else period)
		self.compute_collide()
		self.compute_vel(self.delta_time if not period else period)
	def start(self):
		while(True):
			#possibly use another thread
			self.step(None)
			sleep(self.delta_time/1000)
	def pause(self):
		pass
	def add_body(self,bodies):
		if(isinstance (bodies,list)):
			pass
		else:
			bodies=[bodies]
		for b in bodies:
			assert(isinstance(b,Body))
			self.bodyList.append(b)
	def find(self,x,y):
		'''
		find body with bound including (x,y)
		return None if no body is within the bound
		'''
		for b in self.bodyList:
			if b.get_sq_distance(x,y) < b.mass**2:
				return b
		return None

