import tkinter as tk
from .Space import Space
UPDATE_RATE = 50
 
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
			self.objList.append(self.canvas.create_oval(*AppUtil.getcoordFromMovingBody(body)))
	
	def start(self):
		self.root.mainloop()
	
	def update_state(self):
		'''
		update space first, then update graphics
		'''
		self.space.step()
		for i,body in enumerate(self.space.bodyList):
			bodyCenter=body.loc
			print(bodyCenter)
			self.canvas.coords(self.objList[i],*AppUtil.getcoordFromMovingBody(body))
	def updater(self):
		self.update_state()
		self.canvas.after(UPDATE_RATE, self.updater)
'''
app=Application(space)
app.start()
'''
class AppUtil():
	def getcoordFromMovingBody(body):
		'''
		return: a 4-tuple of the bound of the body accepted 
		        by canvas.create_oval including offset
		'''
		bodyCenter=body.loc
		r=body.radius
		return (bodyCenter.x+r,bodyCenter.y+r,bodyCenter.x+r+10,bodyCenter.y+r+10)