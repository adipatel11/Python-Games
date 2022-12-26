import turtle
import time
import random
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=900, height=730)
screen.title('Hangman')
turtle.tracer(0,0)
def chx(a): 
    t.setx(t.xcor()+a)


face = turtle.Turtle()
neck = turtle.Turtle()
arm1 = turtle.Turtle()
arm2 = turtle.Turtle()
body = turtle.Turtle()
leg1 = turtle.Turtle()
leg2 = turtle.Turtle()
parts = [face,neck,arm1,arm2,body,leg1,leg2]
    
while True:
    t.clear()
    t.ht()
    t.up()
    for part in parts:
        part.ht()
        part.up()
        part.clear()
        part.pensize(2)
    
    neck.goto(200,200)
    chx(-30)
    neck.seth(90)    
    neck.back(30)
    neck.down()
    neck.back(25)
    tempx = neck.xcor()
    tempy = neck.ycor()

    arm1.goto(tempx,tempy)
    arm1.down()
    arm1.seth(315/2)  #arms
    arm1.forward(60)
    arm1.back(60)
    tempx = arm1.xcor()
    tempy = arm1.ycor()

    arm2.goto(tempx,tempy)
    arm2.down()
    arm2.seth(45/2)
    arm2.forward(60)
    arm2.back(60)
    tempx = arm2.xcor()
    tempy = arm2.ycor()

    body.goto(tempx,tempy)
    body.down()
    body.seth(90) #body
    body.back(70)
    tempx = body.xcor()
    tempy = body.ycor()

    leg1.goto(tempx,tempy)
    leg1.down()
    leg1.seth((180+270)/2) #legs
    leg1.forward(70)
    leg1.back(70)
    tempx = leg1.xcor()
    tempy = leg1.ycor()

    leg2.goto(tempx,tempy)
    leg2.down()
    leg2.seth((360+270)/2)
    leg2.forward(70)
    leg2.back(70)
    tempx = leg2.xcor()
    tempy = leg2.ycor()

    t.goto(tempx,tempy)
    t.seth(90)   #----this sets up the hanging structure
    t.up()
    t.forward(155)
    t.down()
    tempx = t.xcor()
    tempy = t.ycor()
    face.goto(tempx,tempy)
    face.seth(180)
    face.down()
    face.circle(30)
    face.up()
    t.color('coral')
    t.pensize(2)
    t.forward(40)
    chx(-100)
    t.back(300)
    chx(50)
    chx(-100)

    t.up()                  #creating the title
    t.goto(-250,230)
    t.color('blue')
    t.down()
    t.write('Hangman!', False, align='left',font=('Arial',50,'normal'))
    t.up()
    turtle.update()

    #from here we have to create categories with different items
    #we do this by creating tuples so they are secure


    cars = ('audi', 'bmw', 'bently', 'ferrari', 'ford', 'honda', 'infiniti',
            'lexus','jeep','acura','bugatti','cadillac','volvo','subaru','ram')

    foods = ('pizza', 'popcorn', 'chocolate', 'cereal','salmon',
             'carrot','cabbage','tofu','almond','coffee','pancake',
             'banana','tomato','cake','steak','burger','chicken',)


    sports = ('football', 'basketball', 'tennis', 'baseball', 'swimming',
              'soccer','archery','bowling','boxing','cricket',
              'badminton','diving')

    ready = input('Welcome to Hangman! Press the enter key to begin playing. ')
    del ready

    
    #now we can choose a random category and a word from that category
    #then we will tell the player which category is chosen


    categories = ('cars', 'foods', 'sports')
    randcat = random.choice(categories)
    if randcat == 'cars':
        word = random.choice(cars)
    elif randcat == 'foods':
        word = random.choice(foods)
    else:
        word = random.choice(sports)
    print()
    print()
    print('The category is ' + randcat + '!')

    #then we proceed to setting up the spaces

    spacing = round(900/(len(word)+len(word)+1))

    t.goto(-450,-200)
    t.color('black')

    for i in range((len(word)+len(word)+1)):
        if i/2 == round(i/2):
            t.up()
            chx(spacing)
        else:
            t.down()
            chx(spacing)

    t.up()
    turtle.update()
    body_breaker = 0
    wincount = 0
    winlist = []

    while True:
        ret = 0
        re = 0
        if wincount == len(word):
            print()
            print('You won!')
            print()
            time.sleep(2)
            break
        print()
        checker = 0
        turtle.update()
        index_counter = 0               
        guess = input('Guess a letter or the word ')
        if guess == word:
            t.color('black')
            print()
            print('You won!')
            print()
            t.up()
            t.goto(-450,-200)
            for i in range((len(word)+len(word)+1)):
                if i/2 == round(i/2):
                    t.up()
                    chx(spacing)
                else:
                    t.down()
                    chx(spacing/2)
                    t.write(word[int(float((i-1)/2))], False, align='center', font=('Arial',spacing,'normal'))
                    chx(spacing/2)
            turtle.update()
            time.sleep(2)
            break
                    
        else:
            for thing in winlist:
                if thing == guess:
                    ret = 1
            if ret == 0:
                winlist.append(guess)
                for letter in word:
                    index_counter = index_counter + 1
                    if guess == letter:
                        re = 1
                        t.color('black')
                        t.up()
                        t.goto(-450,-200)
                        for i in range(index_counter*2):
                            chx(spacing)
                        chx(0-(spacing/2))
                        index_letter = word[(index_counter)-1]
                        t.down()
                        t.write(index_letter, False, align='center', font=('Arial',spacing,'normal'))
                        turtle.update()
                        checker = 1
                        wincount = wincount + 1
                if re == 1:
                    print()
                    print('Nice Guess!')
            else:
                print()
                print("You've already guessed this letter ")
                checker = 1
                
            if checker == 0:                         #break body part if no letter is right
                body_breaker = body_breaker + 1      # or if you don't win
                if body_breaker == 1:
                    leg2.clear()
                elif body_breaker == 2:
                    leg1.clear()
                elif body_breaker == 3:
                    body.clear()
                elif body_breaker == 4:
                    arm2.clear()
                elif body_breaker == 5:
                     arm1.clear()
                elif body_breaker == 6:
                    neck.clear()
                elif body_breaker == 7:
                    face.clear()
                    turtle.update()
                    print('You lost!')
                    print()
                    print('The word was ' + word + '!')
                    print()
                    time.sleep(2)
                    break
                else:
                    pass
