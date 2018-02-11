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
			bodyCenter=body.loc #(x,y)
			self.objList.append(self.canvas.create_oval(bodyCenter.x+5,bodyCenter.y+5,bodyCenter.x+15,bodyCenter.x+15))
	
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
			self.canvas.coords(self.objList[i],bodyCenter.x+5,bodyCenter.y+5,bodyCenter.x+15,bodyCenter.y+15)
		
	def updater(self):
		self.update_state()
		self.canvas.after(UPDATE_RATE, self.updater)
'''
app=Application(space)
app.start()
'''