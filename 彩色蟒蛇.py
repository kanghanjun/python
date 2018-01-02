import turtle
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.pencolor("red")
        turtle.circle(rad, angle)
        turtle.pencolor("black")
        turtle.circle(-rad, angle)
    turtle.pencolor("green")
    turtle.circle(rad, angle/2)
    turtle.pencolor("yellow")
    turtle.fd(rad)
    turtle.pencolor("purple")
    turtle.circle(neckrad+1, 180)
    turtle.pencolor("cyan")
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 700, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    turtle.seth(-40)
    drawSnake(30, 80, 5, pythonsize/2)

main()
