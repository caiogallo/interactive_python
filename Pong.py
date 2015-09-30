# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [10,-10]

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    speedX = random.randrange(120,240) / 60
    speedY = random.randrange(60,180) / 60
   
    if direction == LEFT:        
        ball_vel[0] = -1 * speedX;
        ball_vel[1] = -1 * speedY;
        
    elif direction == RIGHT:
        ball_vel[0] = 1 * speedX;
        ball_vel[1] = -1 * speedY;


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
        
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0
    
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
         
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    if ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] *= -1
    elif ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_vel[1] *= -1
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel >= 0 and paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel <= HEIGHT:
        paddle1_pos += paddle1_vel
   
    if paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel >= 0 and paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel <= HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos - HALF_PAD_HEIGHT],[8,paddle1_pos - HALF_PAD_HEIGHT], [8,paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 1, 'White', 'White')
    canvas.draw_polygon([[WIDTH,paddle2_pos - HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT], [WIDTH-PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, 'White', 'White')
    
    # determine whether paddle and ball collide 
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(LEFT)
            score1 += 1
            
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2 / 2, 80], 32, 'White')
    canvas.draw_text(str(score2), [WIDTH / 2 + WIDTH / 2 / 2, 80], 32, 'White')
        
def keydown(key):
    vel = 4
    
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -vel
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = vel
        
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
            paddle2_vel = 0
    
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
            paddle1_vel = 0

def reset():
    new_game()
            
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
reset = frame.add_button('Reset', reset, 100)

# start frame
new_game()
frame.start()

