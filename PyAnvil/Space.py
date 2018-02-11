from .Body import MovingBody
from .Vector import Vector,Force
from time import sleep
class Space:
	'''
	The whole world
	'''
	def __init__(self,bodyList=[],gravt=Force(0,10,"gravity"),delta_time=50):
		self.bodyList=bodyList
		self.gravt=gravt
		self.delta_time=delta_time
	def __str__(self):
		bodyStr="Bodies:\n"+"\n".join(str(x) for x in self.bodyList) if len(self.bodyList)>0 else "No objects"
		return bodyStr
	def compute_force(self,rate):
		for body in self.bodyList:
			body.update_state(rate)
	def step(self,period=None):
		'''
		Get the space after period ms
		input:
			period:
		'''
		self.compute_force(self.delta_time if not period else period)
	def start(self):
		while(True):
			#possibly use another thread
			self.step(None)
			sleep(self.delta_time/1000)
	def pause(self):
		pass
	def add_body(self,bodies):
		if(isinstance (bodies,list)):
			for b in bodies:
				b.add_force(self.gravt*b.mass)
				self.bodyList.append(b)
		else:
			bodies.add_force(self.gravt*bodies.mass)
			self.bodyList.append(bodies)


