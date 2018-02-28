from PyAnvil import Space,Body,MovingBody,Application,Force,Link

space=Space(gravt=(0,0))
ball=MovingBody(mass=10,init_vel=(0,0),loc=(200,400),id="a")
space.add_body(ball)

ball=MovingBody(mass=10,init_vel=(0,100),loc=(400,450),id="b")
space.add_body(ball)

ball1=MovingBody(mass=10,init_vel=(50,20),loc=(400,400),id="c")
space.add_body(ball1)

ball2=MovingBody(mass=10,init_vel=(100,0),loc=(700,400),id="d")
space.add_body(ball2)


ground=Body(loc=(500,500),dim=(1000,20))
space.add_body(ground)

wall = Body(loc=(500,380),dim=(1000,20), rotate = 0)
space.add_body(wall)

wall1 = Body(loc=(300,430),dim=(200,20), rotate = 45)
space.add_body(wall1)

wall3 = Body(loc=(800,430),dim=(200,20), rotate = 90)
space.add_body(wall3)


block=Body(loc=(200,300),dim=(10,10))
space.add_body(block)
<<<<<<< HEAD
space.add_links(Link.FixedLink(block,ball,magt=100))
=======
space.add_links(Link.ElasticLink(block,ball,magt=100,length=150))

>>>>>>> 923aac9c88d75919c30025ad908e87d6352bf28d
app=Application(space)
app.start()