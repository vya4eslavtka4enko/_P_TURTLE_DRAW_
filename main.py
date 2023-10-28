from turtle import Turtle, Screen

tim = Turtle()

# timmy_the_turtle.shapesize(stretch_len = 3, stretch_wid=2, outline = 2)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)


# for i in range(1,3):
#     tim.forward(200)
#     tim.right(360/3)
# for i in range(1,5):
#     tim.forward(200)
#     tim.right(360/4)
# for i in range(1,6):
#     tim.forward(200)
#     tim.right(360/5)
# for i in range(1,7):
#     tim.forward(200)
#     tim.right(360/6)
# for i in range(1,8):
#     tim.forward(200)
#     tim.right(360/7)
# for i in range(1,9):
#     tim.forward(200)
#     tim.right(360/8)
# for i in range(1,10):
#     tim.forward(200)
#     tim.right(360/9)
step = 3
ang = 2


color = ['red','blue','yellow','brown','green','pink','blue','yellow','brown','green','pink']



for el in range(10):
    step += 1
    ang += 1
    for i in range(1, step):
        tim.forward(100)
        tim.right(360 / ang)
    tim.color(f'{color[i - 1]}')


screen = Screen()
screen.exitonclick()
