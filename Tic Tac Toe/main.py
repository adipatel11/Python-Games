import turtle
import time

screen = turtle.Screen()
screen.setup(width=500,height=500)
screen.title('Tic Tac Toe')
turtle.tracer(0,0)
turtle.bgcolor('black')

t = turtle.Turtle()
b = turtle.Turtle()
b.ht()
b.up()


while True:
    b.goto(-250,250)


    def get_mouse(x, y):
        b.goto(x,y)
        
    def chx(a):
        t.goto(t.xcor()+a,t.ycor())

    def makex(x,y):
        t.up()
        t.color('red')
        t.goto(x,y)
        t.down()
        t.seth((270+360)/2)
        t.forward((500/3)*(2**0.5))
        t.up()
        t.seth(90)
        t.forward(500/3)
        t.down()
        t.seth((180+270)/2)
        t.forward((500/3)*(2**0.5))

    def makecircle(x,y):
        t.color('blue')
        t.seth(90)
        t.up()
        t.goto(x-5,y)
        chx(500/3)
        t.back(500/6)
        t.down()
        t.circle(500/6 - 5)
        
    #setup the board

    t.pensize(3)
    t.ht()
    t.clear()
    t.up()
    t.seth(90)
    t.color('white')

    t.goto(-250,250)

    for i in range(2):
        t.up()
        chx(500/3)
        t.down()
        t.back(500)
        t.forward(500)

    t.up()
    t.goto(-250,-250)

    for i in range(2):
        t.forward(500/3)
        t.down()
        chx(500)
        chx(-500)
        t.up()

    box1 = False
    box2 = False
    box3 = False
    box4 = False
    box5 = False
    box6 = False
    box7 = False
    box8 = False
    box9 = False

    ox1 = ''
    ox2 = ''
    ox3 = ''
    ox4 = ''
    ox5 = ''
    ox6 = ''
    ox7 = ''
    ox8 = ''
    ox9 = ''

    boxes = [ox1,ox2,ox3,ox4,ox5,ox6,ox7,ox8,ox9]

    turtle.update()
    counter = 0

    def xwin():
        t.color('green')
        t.clear()
        t.up()
        t.goto(0,0)
        t.down()
        t.write('X Wins!', move=False,align='center',font=('Arial',70,'normal'))
        turtle.update()
        time.sleep(3)
        
    def ywin():
        t.color('green')
        t.clear()
        t.up()
        t.goto(0,0)
        t.down()
        t.write('Circle Wins!', move=False,align='center',font=('Arial',70,'normal'))
        turtle.update()
        time.sleep(3)


    while True:
        turtle.update()
        if ox1 == 'x' and ox2 == 'x' and ox3 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox1 == 'circle' and ox2 == 'circle' and ox3 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox4 == 'x' and ox5 == 'x' and ox6 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox4 == 'circle' and ox5 == 'circle' and ox6 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox7 == 'x' and ox8 == 'x' and ox9 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox7 == 'circle' and ox8 == 'circle' and ox9 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox1 == 'x' and ox4 == 'x' and ox7 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox1 == 'circle' and ox4 == 'circle' and ox7 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox2 == 'x' and ox5 == 'x' and ox8 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox2 == 'circle' and ox5 == 'circle' and ox8 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox3 == 'x' and ox6 == 'x' and ox9 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox3 == 'circle' and ox6 == 'circle' and ox9 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox1 == 'x' and ox5 == 'x' and ox9 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox1 == 'circle' and ox5 == 'circle' and ox9 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break
        if ox7 == 'x' and ox5 == 'x' and ox3 == 'x':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            xwin()
            break
        if ox7 == 'circle' and ox5 == 'circle' and ox3 == 'circle':
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            ywin()
            break

        if counter == 9:
            for i in range(4):
                t.clear()
                time.sleep(0.3)
                turtle.update()
                t.undo()
                time.sleep(0.3)
                turtle.update()
            t.color('purple')
            t.clear()
            t.up()
            t.goto(0,0)
            t.down()
            t.write('Draw!', move=False,align='center',font=('Arial',80,'normal'))
            time.sleep(3)
            break
            
        turtle.onscreenclick(get_mouse)
        
        if b.xcor() > -250 and b.xcor() < (-250+(500/3)):
            if b.ycor() < 250 and b.ycor() > (250-(500/3)):
                if box1:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex(-250,250)
                        ox1 = 'x'
                    else:
                        makecircle(-250,250)
                        ox1 = 'circle'
                    counter += 1
                    box1 = True
            if b.ycor() < (250-(500/3)) and b.ycor() > (250-(1000/3)):
                if box2:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex(-250,(250-(500/3)))
                        ox2 = 'x'
                    else:
                        makecircle(-250,(250-(500/3)))
                        ox2 = 'circle'
                    counter += 1
                    box2 = True
            if b.ycor() < (250-(1000/3)):
                if box3:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex(-250,(250-(1000/3)))
                        ox3 = 'x'
                    else:
                        makecircle(-250,(250-(1000/3)))
                        ox3 = 'circle'
                    counter += 1
                    box3 = True
        if b.xcor() > (-250+(500/3)) and b.xcor() < (-250+(1000/3)):
            if b.ycor() < 250 and b.ycor() > (250-(500/3)):
                if box4:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex((-250+(500/3)),250)
                        ox4 = 'x'
                    else:
                        makecircle((-250+(500/3)),250)
                        ox4 = 'circle'
                    counter += 1
                    box4 = True
            if b.ycor() < (250-(500/3)) and b.ycor() > (250-(1000/3)):
                if box5:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex((-250+(500/3)),(250-(500/3)))
                        ox5 = 'x'
                    else:
                        makecircle((-250+(500/3)),(250-(500/3)))
                        ox5 = 'circle'
                    counter += 1
                    box5 = True
            if b.ycor() < (250-(1000/3)):
                if box6:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        ox6 = 'x'
                        makex((-250+(500/3)),(250-(1000/3)))
                    else:
                        makecircle((-250+(500/3)),(250-(1000/3)))
                        ox6 = 'circle'
                    counter += 1
                    box6 = True
        if b.xcor() > (-250+(1000/3)):
            if b.ycor() < 250 and b.ycor() > (250-(500/3)):
                if box7:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex((-250+(1000/3)),250)
                        ox7 = 'x'
                    else:
                        makecircle((-250+(1000/3)),250)
                        ox7 = 'circle'
                    counter += 1
                    box7 = True
            if b.ycor() < (250-(500/3)) and b.ycor() > (250-(1000/3)):
                if box8:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex((-250+(1000/3)),(250-(500/3)))
                        ox8 = 'x'
                    else:
                        makecircle((-250+(1000/3)),(250-(500/3)))
                        ox8 = 'circle'
                    counter += 1
                    box8 = True
            if b.ycor() < (250-(1000/3)):
                if box9:
                    pass
                else:
                    if counter/2 == round(counter/2):
                        makex((-250+(1000/3)),(250-(1000/3)))
                        ox9 = 'x'
                    else:
                        makecircle((-250+(1000/3)),(250-(1000/3)))
                        ox9 = 'circle'
                    counter += 1
                    box9 = True






