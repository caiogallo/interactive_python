# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
game_selected = 0;
remainign = 0
msgGuesses = 'Number of remaining guesses is '


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global remaining
    msg = 'New Game. Range is '
    if game_selected == 0:
        range100()
        remaining = 7
        msg += '[0,100)'
    else:
        range1000()
        remaining = 10
        msg += '[0,1000)'
    
    print msg
    print msgGuesses + str(remaining)
    print

# define event handlers for control panel
def range100():
    global secret_number
    secret_number = random.randrange(0, 100)

def range1000():
    global secret_number
    secret_number = random.randrange(0, 1000)
    
def input_guess(guess):
    # main game logic goes here	
    global remaining
    
    iGuess = int(guess)
    remaining = remaining - 1
    
    print 'Guess was ' + guess
    print msgGuesses + str(remaining)
    
    
    if iGuess < secret_number:
        if remaining > 0:
            print 'Higher'
    elif iGuess > secret_number:
        if remaining > 0:
            print 'Lower'
    else:
        print 'Correct'
        print 
        new_game()
    
    if remaining == 0:
        print 'You ran out of guesses. The number was ' + str(secret_number)
    
    
    print
        
def btn1_handler():
    global game_selected
    game_selected = 0
    new_game()
    
def btn2_handler():
    global game_selected
    game_selected = 1
    new_game()
  

# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)

# register event handlers for control elements and start frame
frame.add_input('Input Number', input_guess, 50)
frame.add_button('Range is [0,100)', btn1_handler, 100)
frame.add_button('Range is [0,1000)', btn2_handler, 100)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric

