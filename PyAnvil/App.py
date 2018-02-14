import tkinter as tk
import numpy as np
from .Space import Space


UPDATE_RATE = 50
MARGIN=0 #offsets in the gui
class Application():
	def __init__(self,space:Space):
		self.space=space
		self.shapeList=[]
		self.lineList=[]
		self.setup_tk()
		self.setup_shape()
		
		self.updater()
	
	def setup_tk(self):
		self.root=tk.Tk()
		self.root.title("Space")
		self.canvas=tk.Canvas(self.root,width=1000,height=800)
		self.canvas.pack()
		
	def setup_shape(self):
		for body in self.space.bodyList:
			self.shapeList.append(AppUtil.createShapeFromBody(self.canvas,body))
		for body in self.space.wallList:
			AppUtil.createShapeFromBody(self.canvas,body)
		for link in self.space.links:
			self.lineList.append(AppUtil.createLineFromBody(self.canvas,link))
	
	def start(self):
		self.root.mainloop()
	
	def update_state(self):
		'''
		update space first, then update graphics if the body is movable
		'''
		self.space.step()
		for i,body in enumerate(self.space.bodyList):
			bodyCenter=body.loc
			self.canvas.coords(self.shapeList[i],*AppUtil.getcoordFromBody(body))
		for i ,link in enumerate(self.space.links):
			self.canvas.coords(self.lineList[i],*AppUtil.getcoordFromLink(link))
	def updater(self):
		self.update_state()
		self.canvas.after(UPDATE_RATE, self.updater)
'''
app=Application(space)
app.start()
'''
class AppUtil():
	def createShapeFromBody(canvas,body):
		if(str(body)=="Fixed"):
			return canvas.create_polygon(*AppUtil.getcoordFromBody(body))
		else:#moving bodies
			return canvas.create_oval(*AppUtil.getcoordFromBody(body), )
	
	def getcoordFromBody(body):
		'''
		return: a 8-tuple of the bound of the body accepted 
		        by canvas.create_polygon including offset to represent 4
				corners of the rectangle
		'''
		bodyCenter=np.array((body.loc.x, body.loc.y))
		bodyDim=body.dim
		theta = body.rotate/180 * np.pi
		sin, cos = np.sin, np.cos
		rotMat = np.array([[cos(theta), -sin(theta)],[sin(theta),cos(theta)]])

		ul_x, ul_y = rotMat.dot(np.array([-bodyDim.x/2+MARGIN, -bodyDim.y/2+MARGIN])) + bodyCenter
		ur_x, ur_y = rotMat.dot(np.array([bodyDim.x/2+MARGIN, -bodyDim.y/2+MARGIN])) + bodyCenter
		bl_x, bl_y = rotMat.dot(np.array([-bodyDim.x/2+MARGIN, bodyDim.y/2+MARGIN])) + bodyCenter
		br_x, br_y = rotMat.dot(np.array([bodyDim.x/2+MARGIN, bodyDim.y/2+MARGIN])) + bodyCenter
		if str(body)=="Fixed":
			return (ul_x,ul_y,ur_x,ur_y, br_x, br_y, bl_x, bl_y)
		else:
			return (ul_x,ul_y, br_x, br_y)
		
	def createLineFromBody(canvas,link):
		return canvas.create_line(*AppUtil.getcoordFromLink(link))
	def getcoordFromLink(link):
		target=link.target
		source=link.source
		return (source.loc.x+MARGIN,source.loc.y+MARGIN,
				target.loc.x+MARGIN,target.loc.y+MARGIN)