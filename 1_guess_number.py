# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random 
import math

secret_number = random.randrange(0,100)
num_to_guess = 7
mode = 1


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_to_guess
    if mode == 1:
        secret_number = random.randrange(0,100)
        print "New game. Range is [0,100)"
        print "Number of remaining guesses is 7"
        secret_number = random.randrange(0,100)
        num_to_guess = 7
    else :
        secret_number = random.randrange(0,1000)
        print "New game. Range is [0,1000)"
        print "Number of remaining guesses is 10"
        secret_number = random.randrange(0,1000)
        num_to_guess = 10
    # remove this when you add your code 
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global mode
    mode = 1
    new_game()
    # remove this when you add your code    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global mode
    mode = 2
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, num_to_guess
    num_to_guess -= 1
    print "Guess was " + guess
    print "Number of ramaining guesses is", num_to_guess
    guessnum = int(guess)
    if guessnum < secret_number :
        if num_to_guess > 0 :
            print "Higher!"
        else :
            print "You ran out of guesses.  The number was", secret_number
            print ""
            new_game()
    elif guessnum > secret_number :
        if num_to_guess > 0:
            print "Lower!"
        else :
            print "You ran out of guesses.  The number was", secret_number
            print ""
            new_game()
    else :
        print "Correct!"
        print ""
        new_game()
    print ""
    # remove this when you add your code
    pass

    
# create frame

frame = simplegui.create_frame("Guess the Number!", 200, 200)

# register event handlers for control elements and start frame

button1 = frame.add_button("Range is [0, 100)", range100, 200)
button2 = frame.add_button("Range is [0, 1000)", range1000, 200)
inp = frame.add_input("Enter a guess", input_guess, 200)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
