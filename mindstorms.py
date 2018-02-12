import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    some_turtle.forward(100)
    for i in range(1,3):
        some_turtle.left(120)
        some_turtle.forward(200)
    some_turtle.left(120)
    some_turtle.forward(100)
    

def draw_art():        
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    #brad.speed(2)
    for i in range(1,61):
        draw_triangle(brad)
        brad.right(6)
    brad.right(90)
    #brad.forward(300)

    window.exitonclick()

draw_art()
