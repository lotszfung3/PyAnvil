import tkinter as tk
from .Space import Space
from .Vector import Vector

UPDATE_RATE = 30
MARGIN=0 #offsets in the gui
class Application():
	def __init__(self,space:Space):
		self.space=space
		self.shapeList=[]
		self.setup_tk()
		self.setup_shape()
		self.dragging_body=None
		self.updater()
	
	def setup_tk(self):
		self.root=tk.Tk()
		self.root.title("Space")
		self.canvas=tk.Canvas(self.root,width=1000,height=800)
		self.canvas.pack()
		self.canvas.bind ("<Button-1>", self.down)
		self.canvas.bind ("<ButtonRelease-1>", self.chkup)
		self.canvas.bind("<B1-Motion>",self.mouseDragged)
	def setup_shape(self):
		for body in self.space.bodyList:
			self.shapeList.append(AppUtil.createShapeFromBody(self.canvas,body))
	
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
	def updater(self):
		self.update_state()
		self.canvas.after(UPDATE_RATE, self.updater)
	def down(self,event):
		self.dragging_body=self.space.find(event.x,event.y)
	def chkup(self,event):
		self.dragging_body=None
	def mouseDragged(self,event):
		if self.dragging_body:
			self.dragging_body.loc=Vector(event.x,event.y)
		
class AppUtil():
	def createShapeFromBody(canvas,body):
		return canvas.create_oval(*body.get_coordinates())		
	def createLineFromBody(canvas,link):
		return canvas.create_line(*AppUtil.getcoordFromLink(link))
	def getcoordFromLink(link):
		target=link.target
		source=link.source
		return (source.loc.x+MARGIN,source.loc.y+MARGIN,
				target.loc.x+MARGIN,target.loc.y+MARGIN)