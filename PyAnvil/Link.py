from .Vector import Force
class Link():
	'''
	simulating the force between bodies
	can be of different type: 
	constant force independent of distance,
	link with fixed length,
	link with natural length
	'''
	def __init__(self,source,target,magt):
		'''
		must be between two bodies, with a magt depends of the type
		'''
		self.source=source
		self.target=target
		self.magt=magt
	def update_body_state(self):
		'''
		update the body state
		'''
		raise NotImplementedError()
class FixedLink(Link):
	def update_body_state(self):
		'''
		seems legit to consider the case of cicular motion
		'''
		pass
class ElasticLink(Link):
	#link with natural length
	def __init__(self,source,target,magt=100,length=None):
		super().__init__(source,target,magt)
		if(not length):
			self.length=(source.loc-target.loc).sq_magnitude()**0.5
		else:
			self.length=length
		self.magt=abs(self.magt)
	def update_body_state(self):
		diff_loc=self.target.loc-self.source.loc
		cur_length=diff_loc.sq_magnitude()**0.5
		diff_length=cur_length-self.length
		diff_loc.normalize(self.magt*diff_length/20)#50 is hard coded
		print(diff_loc)
		self.source.update_force(Force(diff_loc.x,diff_loc.y,self.target.id))
		self.target.update_force(Force(-diff_loc.x,-diff_loc.y,self.source.id))
		
		
		
class ConstantLink(Link):
	#link with constant force independent of distance
	def update_body_state(self):
		diff_loc=self.target.loc-self.source.loc
		diff_loc.normalize(self.magt)
		self.source.update_force(Force(-diff_loc.x,-diff_loc.y,self.target.id))
		self.target.update_force(Force(diff_loc.x,diff_loc.y,self.source.id))	