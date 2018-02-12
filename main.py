from PyAnvil import Space,Body,MovingBody,Application,Force

space=Space(gravt=(0,10))
ball=MovingBody(mass=10,init_vel=(10,0),loc=(0,200),id="a")
ball1=MovingBody(mass=10,init_vel=(10,0),loc=(0,300),id="b")
ground=Body(loc=(250,500),dim=(260,100))
space.add_body(ball)
space.add_body(ball1)
space.add_wall(ground)
space.add_links((ball,ball1,-100))
app=Application(space)
app.start()