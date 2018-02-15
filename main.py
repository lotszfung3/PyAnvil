from PyAnvil import Space,Body,MovingBody,Application,Force,Link

space=Space(gravt=(0,0))
ball=MovingBody(mass=10,init_vel=(0,0),loc=(200,400),id="a")
space.add_body(ball)

block=Body(loc=(200,300),dim=(10,10))
space.add_body(block)
space.add_links(Link.FixedLink(block,ball,magt=100))
app=Application(space)
app.start()