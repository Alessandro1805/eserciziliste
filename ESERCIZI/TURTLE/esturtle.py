import turtle
X=-150
Y=100
TOT=360
DIM=50
dim=DIM
x=X
y=Y
finestra=turtle.Screen()
alice = turtle.Turtle()
alice.color("white")
alice.setposition(X,Y)
alice.color("black")
alice.pensize(10)
for i in range(4,13):
    alice.penup()
    alice.setposition(x,y)
    alice.pendown()
    x=x+100
    if(i!=3 and i%3==0):
        y=y-100
        x=X
        dim=DIM-20
    for l in range(0,(i-1)):
        alice.forward(dim)
        alice.right(TOT/(i-1))
turtle.done()