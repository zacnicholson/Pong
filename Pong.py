import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @ZacNicholson")
wn.bgcolor("#d4af37")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_blue = 0
score_purple = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(200)
paddle_a.shape("square")
paddle_a.color("#1b03a3")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(200)
paddle_b.shape("square")
paddle_b.color("#bc13fe")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("#39ff14")
ball.penup()
ball.goto(0, 0)
ball.dx = -2
ball.dy = -2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("#FF6700")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Blue: 0 Purple: 0", align="center", font=("Comic Sans MS", 24, "bold"))




#Fuctions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')

wn.listen()
wn.onkeypress(paddle_a_down, 's')


wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay wet.mov&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay wet.mov&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_blue += 1
        pen.clear()
        pen.write(f" Blue: {score_blue}  Purple: {score_purple}", align="center", font=("Times", 24, "bold"))
        os.system("afplay point.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_purple += 1
        pen.clear()
        pen.write(f" Blue: {score_blue}  Purple: {score_purple}", align="center", font=("Times", 24, "bold"))
        os.system("afplay point.wav&")

    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor()) < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay mm.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor()) < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay hh.wav&")
