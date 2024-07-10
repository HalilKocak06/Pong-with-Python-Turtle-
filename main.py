from turtle import Turtle,Screen
from paddle import Paddle
from Ball import Ball
import time
from scoreboard import Scoreboard



#Ekran düzenlemeleri
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


Ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(0.10)
    screen.update()
    Ball.move()

    if Ball.ycor() > 290 or Ball.ycor() < -290:
        Ball.bounce_y()

    # Sağ paddle gol yer ise
    if Ball.xcor() > 390 :
        Ball.reset_position()
        scoreboard.l_point()
    # sol paddle gol yer ise
    if Ball.xcor() < -390:
        Ball.reset_position()
        scoreboard.r_point()



    if(Ball.distance(r_paddle) < 50 and Ball.xcor() >320) or (Ball.distance(l_paddle) < 50 and Ball.xcor() < -320):
        Ball.bounce_x()    

   


        

screen.exitonclick()