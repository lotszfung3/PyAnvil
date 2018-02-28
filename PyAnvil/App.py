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
			self.canvas.coords(self.shapeList[i],*body.get_coordinates())
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
			return canvas.create_polygon(*body.get_coordinates())
		else:#moving bodies
			return canvas.create_oval(*body.get_coordinates())
			
	def createLineFromBody(canvas,link):
		return canvas.create_line(*AppUtil.getcoordFromLink(link))
	def getcoordFromLink(link):
		target=link.target
		source=link.source
		return (source.loc.x+MARGIN,source.loc.y+MARGIN,
				target.loc.x+MARGIN,target.loc.y+MARGIN)