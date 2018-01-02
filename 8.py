import turtle

def drawSnake(rad,angle,len):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(0)
    drawSnake(100,360,1)

main()
