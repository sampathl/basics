import turtle
def square():
   for i in range(4):
    turtle.forward(100)
    turtle.right(90)

def circle():
    rad=360/24
    for i in range (24):
        square()
        turtle.right(rad)
        
    window.exitonclick()
def triangle():
    for i in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)

def flower():
    rad=120
    for i in range(3):
        triangle()
        turtle.right(rad)
    turtle.right(90)
    turtle.forward(300)
    turtle.write("LS",True,font=("Arial",50,"normal"))
    turtle.exitonclick()

def name(name1):
    turtle.write(name1,True,font=("Arial",50,"normal"))
turtle.color("blue")
turtle.shape("turtle")
#circle()
#triangle()

flower()
#name("LS")

    