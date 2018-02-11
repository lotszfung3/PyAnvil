from PyBullet import Space,Body,Application,Vector

space=Space()

body=Body(mass=10,init_vel=Vector(50,-50),loc=Vector(0,200))

space.add_body(body)

app=Application(space)
app.start()