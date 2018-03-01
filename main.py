from PyAnvil import Space,Body,Application,Vector

space=Space()
bodyList=[Body(10+i) for i in range(50)]
space.add_body(bodyList)

app=Application(space)
app.start()