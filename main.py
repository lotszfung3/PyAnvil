from PyBullet import Space,Body
body=Body(mass=10)
space=Space()
space.add_body(body)
space.start()