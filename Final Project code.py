import turtle                   # for turtle graphics
import random                   # to generate random items
import time                     # to regulate game
import winsound as Wn           # for sound
from sys import exit            # to exit program fully
from tkinter import messagebox  # To create prompt for user


# This function is used to draw a square with its diagonal coordinates
def drawSquare(myTurtle, xlow, ylow, xMax, yMax):
    myTurtle.speed("fastest")  # Make turtle move very fast
    myTurtle.color("white")  # provides color for the coloring
    myTurtle.begin_fill()  # start coloring of the whole shape
    myTurtle.up()  # move without drawing lines
    myTurtle.goto(xlow, ylow)  # move turtle to (x,y) position
    myTurtle.pendown()  # allow the turtle to draw
    myTurtle.goto(xlow, yMax)
    myTurtle.goto(xMax, yMax)
    myTurtle.goto(xMax, ylow)
    myTurtle.goto(xlow, ylow)
    myTurtle.end_fill()  # this ends the painting

# this function draws the dice
def drawdice(dice, x1, y1, x2, y2, dice_number):
    drawSquare(dice, x1, y1, x2, y2)  # draws square for the dice

    # calculate the midpoint of the square
    midX = (x2-x1) / 2
    midY = (y2-y1) / 2

    dice.hideturtle()
    dice.speed("fastest")  # speed up the drawing
    dice.color("black")
    dice.up()
    if dice_number == 1:
        # drwas dice with one dot in the centre
        dice.goto(x1 + midX, y1 + midY)
        dice.dot(size=15)

    elif dice_number == 2:
        # drwas dice with two dots
        dice.goto(x1 + (midX/2), midY + y1)
        dice.dot(size=10)
        dice.goto(x2 - (midX/2), midY + y1)
        dice.dot(size=10)

    elif dice_number == 3:
        # drwas dice with 3 dots on the leading diagonal
        dice.goto(x2 - (midX/3), y2 - (midY/3))
        dice.dot(size=7)
        dice.goto(x1 + midX, y1 + midY)
        dice.dot(size=7)
        dice.goto(x1 + (midX/3), y1 + (midY/3))
        dice.dot(size=7)

    elif dice_number == 4:
        # drwas dice with 4 dots
        dice.goto(x2 - (midX/3), y2 - (midY/3))
        dice.dot(size=10)
        dice.goto(x2 - (midX/3), y1 + (midY/3))
        dice.dot(size=10)
        dice.goto(x1 + (midX/3), y1 + (midY/3))
        dice.dot(size=10)
        dice.goto(x1 + (midX/3), y2 - (midY/3))
        dice.dot(size=10)

    elif dice_number == 5:
        # draws dice with 5 dots
        dice.goto(x2 - (midX/3), y2 - (midY/3))
        dice.dot(size=8)
        dice.goto(x2 - (midX/3), y1 + (midY/3))
        dice.dot(size=8)
        dice.goto(x1 + (midX/3), y1 + (midY/3))
        dice.dot(size=8)
        dice.goto(x1 + (midX/3), y2 - (midY/3))
        dice.dot(size=8)
        dice.goto(x1 + midX, y1 + midY)
        dice.dot(size=8)

    else:
        # drwas dice with 6 dots
        dice.goto(x2 - (midX/3), y2 - (midY/3))
        dice.dot(size=8)
        dice.goto(x2 - (midX/3), y1 + (midY/3))
        dice.dot(size=8)
        dice.goto(x1 + (midX/3), y1 + (midY/3))
        dice.dot(size=8)
        dice.goto(x1 + (midX/3), y2 - (midY/3))
        dice.dot(size=8)
        dice.goto(x1 + (midX/3), midY + y1)
        dice.dot(size=8)
        dice.goto(x2 - (midX/3), midY + y1)
        dice.dot(size=8)


def Terminate_game(dice,Scr):
    dice.color("white")
    dice.goto(-210, 20)
    # writes these on the screen
    dice.write("GAME OVER", font=("Helvetica", 55, "bold"))
    dice.goto(-210, -90)
    dice.write(
        "CLICK ANYWHERE \n TO EXIT", font=("Arial", 30, "italic")
    )
    Scr.exitonclick()
    exit()  # ends the program in the while loop


# this is the game's program for each level
def program( dice, game_level, picture):
    Wn.PlaySound("background.wav", Wn.SND_FILENAME | Wn.SND_ASYNC) # adds background sound
    if game_level in {1,2}: # instructions for level 1 and 2
        
        # generating a list of various positions for dice on same line
        positions_list = [((x, 0), (x + 60, 60)) for x in range(-200, 200, 70)]
    else:
        # generating a list of various positions for dice 
        # at random position on screen
        positions_list = [
            ((x, y), (x + 60, y + 60))
            for x in range(-200, 200, 70)
            for y in range(-200, 200, 70)
        ]

    Scr = turtle.Screen()
    dice.up()

    while True:  # Allows the user to repeat a level several times
        Scr.bgpic(picture)
        time.sleep(1.1)
        acc = 0
        # 'll' = lower left coordinates and 'ur' = upper right coordinates
        Wn.PlaySound("Dice 03.wav", Wn.SND_FILENAME | Wn.SND_ASYNC) # adds background sound
        for ll, ur in random.sample(positions_list, random.randint(2,5)):
            dice_num = random.randint(1, 6)
            drawdice(
                dice,
                *ll, # unpacks all the generated lower coordinates 
                *ur, # unpacks all the generated upper coordinates
                dice_num
            )
            
            acc += dice_num
        
        time.sleep(4.01)
        Scr.clearscreen()  # clears the screen after time in sleep()
        Scr.bgcolor("black")  # black screen background

        Wn.PlaySound("background.wav", Wn.SND_FILENAME | Wn.SND_ASYNC) # adds background sound
        answer = Scr.numinput(
            "Whats the sum?", "Enter your answer"
        )
        
        if answer == acc:
            Wn.PlaySound("winning.wav", Wn.SND_FILENAME | Wn.SND_ASYNC)
            Scr.bgpic("congrat.gif")
            dice.write(" ")
            time.sleep(2.5)  # show congratulation picture for 1 sec

            repeat = Scr.numinput(
                "MATHEMATICIAN",
                "1. New game\n2. Exit game",
                minval=1,
                maxval=2
            )

            Scr.clearscreen()
            Scr.bgcolor("black")
            # check user input and carry corresponding action
            if repeat == 1:
                Game()  # restart game

            else:
                Terminate_game(dice,Scr)
                
        else:
            Wn.PlaySound("losing.wav", Wn.SND_FILENAME | Wn.SND_ASYNC)
            repeat = Scr.numinput(
                "GOOD ATTEMPT ",
                "TRY AGAIN \nPRESS \n1. Restart\n2. Quit",
                minval=1,
                maxval=2,
            )

            Scr.clearscreen()
            Scr.bgcolor("black")  # clear screen and set it to black
            if repeat == 1:
                time.sleep(0.5)

            else:
                Terminate_game(dice,Scr)

# This is the game funcion
def Game():
    Wn.PlaySound("background.wav", Wn.SND_FILENAME | Wn.SND_ASYNC) # adds background sound
    dice = turtle.Turtle()
    dice.color("white")
    dice.hideturtle()

    Scr = turtle.Screen()
    # pops up an onscreen entry box to choose level
    level = Scr.numinput(
        "Choose level", "1. Easy\n2. Medium\n3. Hard\n", minval=1, maxval=3
    )
    # checking selected level
    if level == 1:
        program( dice, 1, "easy.gif") # calls program function

    elif level == 2:
        program( dice, 2, "medium.gif")

    elif level == 3:
        program( dice, 3, "hard.gif")

# This function gives the game's starting interface
# and then calls the game function.
def RunGame():
     # forming my turtle
    artist = turtle.Turtle()
    artist.up()
    artist.speed("fastest")    
    artist.color("white")
    artist.hideturtle()

    Wn.PlaySound("background.wav", Wn.SND_FILENAME | Wn.SND_ASYNC) # adds background sound
    
    art = turtle.Turtle()
    art.speed("fastest")
    art.pencolor("violet")  # the loading bar's color
    art.hideturtle()

    Scr = turtle.Screen()
    Scr.bgpic("firstpage.gif")  # inserts this picture when the program starts
    artist.write("")
    time.sleep(2.5)  # pauses for 1 second
    Scr.clearscreen()  # clears the screen after time in sleep()
    Scr.bgcolor("black")  # black screen background

    repeat = messagebox.askyesno("HOLA AMIGO.... ", # title
                                 " Are you Ready? ") # prompt
    default_response = True
    if repeat == default_response:
        shift = 50
        art.up()
        art.goto(-250, 0)
        art.down()
        art.goto(-250, 0)
        # Creates the loading game interface
        for i in range(0, 110, 50):
            art.pensize(30)  # make the pensize bigger
            art.goto(-200 + shift, 0)
            artist.goto(-300, -90)

            # writes on the screen
            artist.write(f"loading game......{i}%", font=("Arial", 40, "bold"))
            time.sleep(0.1)
            artist.clear()  # clears writings after 0.5 seconds

            shift += 200  # increases length of loading bar

        art.clear()  # clears the drawing of the bar

        # inserts colorful background pic
        Scr.bgpic("Intro.gif") 
        artist.write("")
        time.sleep(3.5)  # pauses for 1 second
        Scr.clearscreen()  # clears the screen after time in sleep()
        Scr.bgcolor("black")  # black screen background

        artist.goto(-300, -90)
        # writing to the screen
        artist.write(
             " How fast can you add 🧐\n\n", font=("Helvetica", 35, "bold")
         )
        time.sleep(2.5)
        artist.clear()  # clears the writing after 2.5 seconds
        
        # writes something to the screen
        artist.write(
                f'''
                
            Clue:
            
         Add the number
            of dots
         On each dice
            
    Time allocated:  4 seconds ''',
            font=("Helvetica", 30, "bold")
        )
        
        time.sleep(5)
        artist.clear()  # clears the writing after 5 seconds

        Game()  # calls the game function
        
    else:
        # writes on the screen
        artist.goto(-240, -10)
        artist.write(
            "Okay then......\nSee you later\n", font=("Helvetica", 48, "bold")
        )
        artist.goto(-240, -100)
        artist.write("CLICK ANYWHERE \n TO EXIT", font=("Arial", 30, "italic"))

        # close the graphics when it is clicked
        Scr.exitonclick()

if __name__ == "__main__":
    RunGame()  # runs this only from this module