from PyAnvil import Space,MovingBody,Application,Vector

space=Space()

body2=MovingBody(mass=10,init_vel=Vector(0,0),loc=Vector(0,0))
space.add_body(body2)

app=Application(space)
app.start()