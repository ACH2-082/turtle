import turtle
import random

win = turtle.Screen()
win.bgcolor("white")
win.setup(width=750 , height=550)

finish_line = turtle.Turtle()
finish_line.up()
finish_line.goto(160,100)
finish_line.down()
finish_line.goto(160,-100)
finish_line.hideturtle()

finish = turtle.Turtle()
finish.hideturtle()
finish.up()
finish.goto(180,-50)
finish.down()
finish.write("F\nI\nN\nI\nS\nH", align="center",font=("Courier",14,"bold"))

turtles = []
colors = ["blue", "gold", "green", "orange", "red",]
for i in range(5):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.up()
    t.goto(-175,50-i*25)
    t.down()
    turtles.append(t)
    
winner = None
while winner == None:

    for t in turtles:
        t.forward(random.randint(1,5))
        if t.xcor() >= 150:
            winner = t
        
        
winner.goto(0,75)
winner.write("turtle number {} is the winner!".format(colors.index(winner.color()[0])+1),align="center",font=("Courier",14,"bold")    )















