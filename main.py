from PyAnvil import Space,Body,MovingBody,Application

space=Space()
ball=MovingBody(mass=10,init_vel=(20,-20),loc=(0,200))
space.add_body(ball)

app=Application(space)
app.start()