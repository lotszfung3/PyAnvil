from PyAnvil import Space,Body,MovingBody,Application

space=Space()
ground=Body(loc=(250,300),dim=(260,100))
ball=MovingBody(mass=10,init_vel=(0,0),loc=(0,0))
space.add_body(ball)
space.add_wall(ground)

app=Application(space)
app.start()