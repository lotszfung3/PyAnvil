from PyAnvil import Space,Body,Application,Vector

space=Space()
bodyList=[Body(id=i,mass=10 + 2 * i,group_id=i%3) for i in range(9)]
space.add_body(bodyList)

app=Application(space)
app.start()