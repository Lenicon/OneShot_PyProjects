import turtle
import time
import random
from subprocess import Popen
import pyautogui
from tkinter import *
import msvcrt


#disable keyboard class
class keyboardDisable():

    def start(self):
        self.on = True
    
    def stop(self):
        self.on = False
    
    def __call__(self):
        while self.on:
            msvcrt.getwch()
    
    def __init__(self):
        self.on = False
        import msvcrt


delay = 0.1
score = 0
high_score = 0
threshold_score = 1
confirmation = "None"
 
# Creating a window screen
wn = turtle.Screen()
wn.title("Sanek Ballsack uwu")
wn.bgcolor("black")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)
 
# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'orange'])
food.speed(0)
food.shape('circle')
food.color(colors)
food.penup()
food.goto(0, 100)
 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
 
 
# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
 
segments = []

def onclick_yes():
    confirmation = "Yes"
    pen.clear()
    time.sleep(0.1)
    pen.write("Thanks baby! xoxo i luv u uwu xoxo\ni love when u suck my bals wet~ ahh~", align="center", font=("candara", 16, "bold"))
    
    time.sleep(2)
    link="https://rule34.xxx/index.php?page=post&s=view&id=5903066"
    Popen(f"cmd /c start chrome {link} --new-window")
    time.sleep(5)
    exit()

def onclick_no():
    confirmation = "Yes"
    pen.clear()
    pen.write("I fuckin hate u\nill hack ur computer u scum", align="center", font=("candara", 16, "bold"))
    timeout = time.time()+60*2
    while True:
        if time.time() > timeout:
            pen.clear()
            pen.write("bitch loser", align="center", font=("candara", 22, "bold"))
            time.sleep(2)
            keyboardDisable.stop()
            time.sleep(0.1)
            exit()
            break
        pyautogui.moveTo(350, 350)
        keyboardDisable().start()
        
FONT_SIZE=20
CURSOR_SIZE=20

canvas = wn.getcanvas()

# Main Gameplay
while True:
    wn.update()

    #ask a prompt when reaching the score threshold
    if score >= threshold_score:
        pen.clear()
        pen.write("Will you gobble my ballsack uwu?", align="center", font=("candara", 16, "bold"))
        yesbutton = Button(canvas.master, text="Yes plz yum!!", command=onclick_yes)
        nobutton = Button(canvas.master, text="no cuz im faggot", command=onclick_no)

        yesbutton.pack()
        nobutton.pack()
        yesbutton.place(x=150, y=300)
        nobutton.place(x=450, y=300)
    elif confirmation != "None":
        break
    else:
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)
    
            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("yellow")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        # Checking for head collisions with body segments
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
    
                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
wn.mainloop()