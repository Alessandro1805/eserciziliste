import turtle
import random
TIME=7200
def pazzia():
    robot=turtle.Turtle()
    finestra=turtle.Screen()
    robot.penup()
    robot.setposition(0,0)
    robot.pendown()
    robot.pensize(2000)
    for _ in range(0,7200):
        robot.right(random.randrange(0,4)*90)
        robot.forward(25)
        robot.speed(0)
    turtle.done()
def main():
    pazzia()

if __name__=="__main__":
    main()
