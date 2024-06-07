from turtle import *

# we want to paint a house 

# step1:draw a square
speed(20)
width(7)
color("gold")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

# step:2 drawing door
forward(70)
color("brown")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()
#end of the door

penup()
goto(200,200)
pendown()
#drawing roof
color("magenta")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing roof done

#drawing windows
color("blue")
begin_fill()
penup()
goto(150,150)
pendown()
left(30)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
end_fill()
#right window done
#start of the left window

color("blue")
begin_fill()
penup()
left(180)
goto(20,150)
pendown()
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
end_fill()
#end of windows
#starting grass field
color("green")
penup()
begin_fill()
goto(-475,-100)
pendown()
left(180)
forward(945)
right(90)
forward(290)
right(90)
forward(945)
right(90)
forward(290)
end_fill()












exitonclick()

