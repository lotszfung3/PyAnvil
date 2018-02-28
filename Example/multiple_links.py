from PyAnvil import Space,Body,MovingBody,Application,Force,Link

space=Space(gravt=(0,0))
balla=MovingBody(mass=10,init_vel=(0,0),loc=(200,400),id="a")
ballb=MovingBody(mass=10,init_vel=(0,0),loc=(200,200),id="b")
ballc=MovingBody(mass=10,init_vel=(0,0),loc=(300,300),id="c")
balld=MovingBody(mass=10,init_vel=(0,0),loc=(100,300),id="d")
space.add_body([balla,ballb,ballc,balld])


block=Body(loc=(200,300),dim=(10,10))
space.add_body(block)

space.add_links(Link.ConstantLink(block,balla,magt=-50))
space.add_links(Link.ConstantLink(block,ballb,magt=-50))
space.add_links(Link.ConstantLink(block,ballc,magt=-50))
space.add_links(Link.ConstantLink(block,balld,magt=-50))
app=Application(space)
app.start()