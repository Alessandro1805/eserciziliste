import turtle
X=-150
Y=100
TOT=360
DIM=50
def draw(x,y,dim):
    disegno=turtle.Turtle()
    finestra=turtle.Screen()
    disegno.penup()
    disegno.setposition(x,y)
    disegno.pendown()
    disegno.pensize(5)
    for i in range(4,13):
        disegno.penup()
        disegno.setposition(x,y)
        disegno.pendown()
        disegno.begin_fill()
        disegno.color("black")
        x=x+100
        if(i!=3 and i%3==0):
            y=y-100
            x=X
            dim=DIM-20
        for l in range(0,(i-1)):
            disegno.forward(dim)
            disegno.right(TOT/(i-1))
        disegno.color("light blue");
        disegno.end_fill()
    turtle.done()

def main():
    dim=DIM
    x=X
    y=Y
    draw(x,y,dim)
if __name__=="__main__":
    main()