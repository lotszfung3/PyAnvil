from .Body import MovingBody,Body
from .Vector import Vector,Force
from .Impact import Impact
from typing import List
from time import sleep
class Space:
	'''
	The whole world
	'''
	def __init__(self,bodyList=[],gravt=(0,10),delta_time=50):
		self.bodyList=bodyList
		self.wallList=[]
		self.links=[]
		self.gravt=Force(gravt[0],gravt[1],"gravity")
		self.delta_time=delta_time
	def __str__(self):
		bodyStr="Bodies:\n"+"\n".join(str(x) for x in self.bodyList) if len(self.bodyList)>0 else "No objects"
		return bodyStr
	def compute_force(self,rate):
		for body in self.bodyList:
			body.update_state(rate)
	def compute_links(self):
		for link in self.links:
			Impact.linkForceWithBody(link[0],link[1],link[2])
	def detect_collide(self):
		'''
		if detected body collision between moving body and wall, update velocity
		'''
		for body in self.bodyList:
			Impact.bodyCollideWithWall(body,self.wallList)
	def step(self,period=None):
		'''
		Get the space after period ms
		input:
			period:
		'''
		self.compute_force(self.delta_time if not period else period)
		self.detect_collide()
		self.compute_links()
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
				b.update_force(self.gravt*b.mass)
				self.bodyList.append(b)
		else:
			bodies.update_force(self.gravt*bodies.mass)
			self.bodyList.append(bodies)
	def add_wall(self,bodies):
		if(isinstance (bodies,list)):
			for b in bodies:
				self.wallList.append(b)
		else:
			self.wallList.append(bodies)
	def add_links(self,links):
		if(isinstance(links,list)):
			for l in links:
				self.links.append(l)
		else:
			self.links.append(links)


