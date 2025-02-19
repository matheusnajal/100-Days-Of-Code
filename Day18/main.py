import turtle as turtle_module
import random

colors = [(198, 32, 13), (248, 25, 236), (40, 188, 76), (39, 69, 216), (238, 5, 227), (227, 49, 159), (29, 154, 40), (212, 15, 76), (17, 17, 153), (241, 161, 36), (195, 12, 16),
 (223, 120, 21), (68, 31, 10), (61, 8, 15), (223, 206, 141), (11, 62, 97), (219, 11, 159), (54, 229, 209), (19, 49, 21), (238, 216, 157), (79, 212, 74), (10, 238, 228), (73, 168, 212), (93, 198, 233), (65, 239, 231), (217, 51, 88)]
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_dots = 100

for dot_count in range(1, number_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()