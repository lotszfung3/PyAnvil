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
	def __init__(self,source,target,magt):
		super().__init__(source,target,magt)
		self.length=(source.loc-target.loc).sq_magnitude()**0.5
	def update_body_state(self):
		'''
		seems legit to consider the case of cicular motion
		'''
		self_dir=self.source.loc-self.target.loc
		# f1:get force with same direction as the link
		other_force=self.target.get_res_force().projection_in(self_dir)
		# v: instaneous velocity tangential to the link 
		target_vel=self.target.velocity.perpedicular_in(self_dir)
		#f=self.target.mass *  v**2 /(self.length) +f1
		target_force=self.target.mass*target_vel.sq_magnitude() /self.length - other_force
		self.source.update_force(Force(target_force.x,target_force.y,self.target.id))
		self.target.update_force(Force(-target_force.x,-target_force.y,self.source.id))
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