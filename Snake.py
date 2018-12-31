#Snake by Viren W

import turtle
import time
import random

d = 0.1 

#Initializes Score
score = 0
highScore = 0

#Screen Setup
Window = turtle.Screen()
Window.title("Snake by Viren")
Window.bgcolor("white")
Window.setup(width = 700, height = 700)
Window.tracer(0)

#Snake Head
TurtleHead = turtle.Turtle()
TurtleHead.speed(0)
TurtleHead.shape("square")
TurtleHead.color("gray")
TurtleHead.penup()
TurtleHead.goto(0,0) #Sets turtle to Center of Screen
TurtleHead.direction = "stop"

#Snake Food
TurtleFood = turtle.Turtle()
TurtleFood.speed(0)
TurtleFood.shape("circle")
TurtleFood.color("red")
TurtleFood.penup()
TurtleFood.goto(0,100) #Sets turtle food on screen

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0) #Animation Speed
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,320)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 22, "normal"))

#Functions
def go_up():
    if TurtleHead.direction != "down":

        TurtleHead.direction  = "up"
def go_down():
    if TurtleHead.direction != "up":
        TurtleHead.direction  = "down"
def go_left():
    if TurtleHead.direction != "right":
        TurtleHead.direction  = "left"
def go_right():
    if TurtleHead.direction != "left":
        TurtleHead.direction  = "right"
def move():
    if TurtleHead.direction == "up":
        y = TurtleHead.ycor()
        TurtleHead.sety(y+20)

    if TurtleHead.direction == "down":
        y = TurtleHead.ycor()
        TurtleHead.sety(y-20)

    if TurtleHead.direction == "left":
        x = TurtleHead.xcor()
        TurtleHead.setx(x-20)

    if TurtleHead.direction == "right":
        x = TurtleHead.xcor()
        TurtleHead.setx(x+20)    

#Binding Keyboard to Game
Window.listen()
Window.onkeypress(go_up, "Up")
Window.onkeypress(go_down, "Down")
Window.onkeypress(go_left, "Left")
Window.onkeypress(go_right, "Right")


while True:
    Window.update() #updates screen

    #Checks for collisio with wall(s)
    if TurtleHead.xcor() > 340 or TurtleHead.xcor() < -340 or TurtleHead.ycor() > 340 or TurtleHead.ycor() < -340:
        time.sleep(1)
        TurtleHead.goto(0,0)
        TurtleHead.direction = "stop"

        for segment in segments: #Goes through each segment
            segment.goto(1000,1000) #Hides segments when you "die"
        
        #Clears list
        segments.clear() 

        #Resets Score
        score = 0
        
        #Reset Delay
        d = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center", font = ("Courier", 22,"normal"))

    
    #Checks for collision between food and head
    if TurtleHead.distance(TurtleFood) < 15: 
        #Move food to random spot
        x = random.randint(-340,340)
        y = random.randint(-340,340)
        TurtleFood.goto(x,y)  

        #Adds a segment when you touch the food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment) 

        #Shortens Delay // Game speeds up as score increases 
        d = d - 0.001
        #Increases the Score
        score = score + 1 
    
        if score > highScore:
            highScore = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center", font = ("Courier", 22,"normal"))
    #Moves the end segments first in reverse order  
    for i in range(len(segments)-1,0,-1): #decrements each time by 1
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments) > 0:
        x = TurtleHead.xcor()
        y = TurtleHead.ycor()
        segments[0].goto(x,y)
    
    move()

    #Checks for head collision w/ body

    for segment in segments:
        if segment.distance(TurtleHead) < 20:
            time.sleep(1)
            TurtleHead.goto(0,0)
            TurtleHead.direction = "stop"

             
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            #Resets Score
            score = 0

            #Reset Delay
            d = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center", font = ("Courier", 22,"normal"))

    time.sleep(d)

Window.mainloop()
