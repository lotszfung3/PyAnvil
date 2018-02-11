A programming project aims to develop a 2D physics engine from scratch and features by features using Python with the aims to train skills on OOP, software development and possibly physics knowledge.

A wiki page  may be added later when the features are more well developed.

There are mainly 2 components, the physics engine and simple GUI used to show the movement.

# Steps to quick start:
1. import stuff
```
from PyBullet import Space,Body,Application,Vector
```
2. create the space
```
space=Space()
```
3. create body and add to the space
```
body=MovingBody(mass=10,init_vel=Vector(50,-50),loc=Vector(0,200))
space.add_body(body)
```
4. create gui application and start
```
app=Application(space)
app.start()
```

## Features have developed:
- Gravitation
- Point body
- GUI that can only draw circle body

## Features to be implemented:
- The Graphics matching each features
- Constant Force(Link) between 2 objects
- Attractive/Repulsive Force among objects
- Body with area (rectangle, circle)
- A fixed body in the space (ground)
- Collision among body
- Friction(air resistance/ friction on floor)
- Rotating movement
- Joint/Hinge

