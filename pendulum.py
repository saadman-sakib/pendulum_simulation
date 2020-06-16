from turtle import*
from math import*
from time import*
g=9800000 #accelaration due to gravity(used a big amount to simulate the pendulum faster)

tracer(0)
hideturtle()

def main():
    length = 15.0           # Of pendulum (meters)
    ngol = - g / length     # n-g-o-l=Negative G over L
    total_time = 0.0        # Seconds
    angle = 1.0             # Initial angle of pendulum (radians)
    speed = 0.0             # Initial angular velocity (radians/second)
    time_step = 0.00001     # Seconds
    while True:
        total_time += time_step
        speed += ngol * sin(angle)* time_step
        angle += speed * time_step
        draw(angle, length)
        sleep(time_step)



def draw(angle, length):
    clear()
    goto(0,250)  #pivot point's co-ordinate
    dot(length*2)    #pivot point's size
    setheading(angle*180/pi+270)   #initial angle og pendulum
    pensize(max(round(length), 1))  #shape of the stick
    pendown()
    forward(length * 25)  #length of the stick
    penup()
    dot(length * 10) #bob size
    home()
    update()

main()
done()
