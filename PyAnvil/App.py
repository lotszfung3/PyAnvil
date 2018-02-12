import tkinter as tk
from .Space import Space
UPDATE_RATE = 50
MARGIN=10 #offsets in the gui
class Application():
	def __init__(self,space:Space):
		self.space=space
		self.objList=[]
		
		self.setup_tk()
		self.setup_shape()
		
		self.updater()
	
	def setup_tk(self):
		self.root=tk.Tk()
		self.root.title("Space")
		self.canvas=tk.Canvas(self.root,width=500,height=500)
		self.canvas.pack()
		
	def setup_shape(self):
		for body in self.space.bodyList:
			self.objList.append(AppUtil.createShapeFromBody(self.canvas,body))
		for body in self.space.wallList:
			self.objList.append(AppUtil.createShapeFromBody(self.canvas,body))
	
	def start(self):
		self.root.mainloop()
	
	def update_state(self):
		'''
		update space first, then update graphics if the body is movable
		'''
		self.space.step()
		for i,body in enumerate(self.space.bodyList):
			if(body.movable):
				bodyCenter=body.loc
				print(bodyCenter)
				self.canvas.coords(self.objList[i],*AppUtil.getcoordFromBody(body))
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
			return canvas.create_rectangle(*AppUtil.getcoordFromBody(body))
		else:#moving bodies
			return canvas.create_oval(*AppUtil.getcoordFromBody(body))
	def getcoordFromBody(body):
		'''
		return: a 4-tuple of the bound of the body accepted 
		        by canvas.create_oval including offset
		'''
		bodyCenter=body.loc
		bodyDim=body.dim
		return (bodyCenter.x-bodyDim.x+MARGIN,bodyCenter.y-bodyDim.y+MARGIN,
				bodyCenter.x+bodyDim.x+MARGIN,bodyCenter.y+bodyDim.y+MARGIN)