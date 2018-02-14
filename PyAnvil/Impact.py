from .Vector import Force
class Impact:
	'''
	class include functions to calculate the impact of collision and other physics stuff
	'''
	def bodyCollideWithWall(body,wallList):
		'''
		simply update velocity if within bound, may become complicated later
		TODO: extend if the wall is not vertical or horizontal
		'''
		for wall in wallList:
			if(Impact.withinBound(body.loc,wall)):
				body.velocity.y = -body.velocity.y
				
	def withinBound(bodyPoint,wall):
		'''
		return 2-tuple to multiply to the
		'''
		wallBound=(wall.loc.x-wall.dim.x,wall.loc.y-wall.dim.y,
					wall.loc.x+wall.dim.x,wall.loc.y+wall.dim.y)
		return bodyPoint.x>=wallBound[0] and bodyPoint.x<=wallBound[2] and bodyPoint.y>=wallBound[1] and bodyPoint.y<=wallBound[3]
	def linkForceWithBody(bodyA,bodyB=None,magt=0):
		'''
		add constant force between bodies with link
		'''
		diff_loc=bodyB.loc-bodyA.loc
		diff_loc.normalize(magt)
		print(diff_loc)
		bodyA.update_force(Force(-diff_loc.x,-diff_loc.y,bodyB.id))
		bodyB.update_force(Force(diff_loc.x,diff_loc.y,bodyA.id))		
		