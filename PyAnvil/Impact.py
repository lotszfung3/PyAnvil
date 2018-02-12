class Impact:
	'''
	class include functions to calculate the impact of collision and other physics stuff
	'''
	def bodyCollideWithWall(body,wallList):
		'''
		simply update velocity if within bound, may become complicated later
		'''
		for wall in wallList:
			if(Impact.withinBound(body.loc,wall)):
				body.velocity=-body.velocity
	def withinBound(bodyPoint,wall):
		wallBound=(wall.loc.x-wall.dim.x,wall.loc.y-wall.dim.y,
					wall.loc.x+wall.dim.x,wall.loc.y+wall.dim.y)
		return bodyPoint.x>=wallBound[0] and bodyPoint.x<=wallBound[2] and bodyPoint.y>=wallBound[1] and bodyPoint.y<=wallBound[3]