from .Vector import Force
import numpy as np


MARGIN=5 #offsets in the gui

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
				body.velocity.x , body.velocity.y = Impact.body_wall_collision(body, wall)
				
	def withinBound(bodyPoint,wall):
		'''
		consider the coordinates of the body in the rotated system 
		'''	
		wallBound= (wall.loc.x-wall.dim.x/2, wall.loc.y-wall.dim.y/2, wall.loc.x+wall.dim.x/2, wall.loc.y+wall.dim.y/2)
		theta = wall.rotate
		x,y = np.array([[np.sin(theta), np.cos(theta)],[-np.sin(theta), np.cos(theta)]]).dot(np.array((bodyPoint-wall.loc).to_tuple())) + np.array(wall.loc.to_tuple())
		return (x>=wallBound[0]-MARGIN and x<=wallBound[2]+MARGIN and y>=wallBound[1]-MARGIN and y<=wallBound[3]+MARGIN)
					
				
	def linkForceWithBody(bodyA,bodyB=None,magt=0):
		'''
		add constant force between bodies with link
		'''
		diff_loc=bodyB.loc-bodyA.loc
		diff_loc.normalize(magt)
		bodyA.update_force(Force(-diff_loc.x,-diff_loc.y,bodyB.id))
		bodyB.update_force(Force(diff_loc.x,diff_loc.y,bodyA.id))		
	
	def body_wall_collision(body, wall):
		#Coefficient of restitution: fixed now, can be an attribute of the body in the future
		e = 0.9
		
		# Theta : angle of inclination of the wall
		theta = wall.rotate

		# v_ix, v_iy: initial velocity along the plane and perpendicular to the plane
		
		r = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
		v_ix, v_iy = r.dot(np.array(body.velocity.to_tuple()))
						
		# update velocity
		v_iy *= -e
		r = r.T
		
		return r.dot(np.array([v_ix, v_iy]))		