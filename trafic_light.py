import turtle

wn =  turtle.Screen()
wn.title("stop light by droobi")
wn.bgcolor("black")



pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30,60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

red_light = turtle.Turtle()
red_light.shape ("circle")
red_light.color("white")
red_light.penup()
red_light.goto(0,40)


yellow_light =turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("white")
yellow_light.penup()
yellow_light.goto(0,0)


green_light =turtle.Turtle()
green_light.shape("circle")
green_light.color("white")
green_light.penup()
green_light.goto(0,-40)




import time

while True :
    red_light.color("red")
    time.sleep(2)

    green_light.color("white")
    red_light.color("red")
    yellow_light.color("yellow")
    time.sleep(1)

    green_light.color("white")
    red_light.color("white")
    yellow_light.color("yellow")
    time.sleep(2)

    red_light.color("white")
    yellow_light.color("white")
    green_light.color("green")
    time.sleep(3)



    green_light.color("white")




