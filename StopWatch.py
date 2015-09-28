# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
attemps = 0
success = 0
start = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t%10
    c = (t/10)%10
    b = ((t/10)/10)%6
    a = (((t/10)/10)/6)%24
       
    formattedTime = str(a) + ':' + str(b) + str(c) + '.'+str(d)
    
    return formattedTime

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global start
    start = True
    timer.start()

def stop_handler():
    global start, attemps, success
    
    if(start == True):
        attemps += 1
        
        if((time%10) == 0):
            success += 1
    
    start = False
        
    timer.stop()

def reset_handler():
    global time, attemps, success
    timer.stop()
    time = 0
    attemps = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):    
    canvas.draw_text(format(time), (120, 150), 32, 'White')
    canvas.draw_text(str(success) + '/' + str(attemps), (270, 20), 22, 'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 300, 300)


# register event handlers
timer = simplegui.create_timer(100, time_handler)
start = frame.add_button('Start', start_handler, 100)
stop = frame.add_button('Stop', stop_handler, 100)
reset = frame.add_button('Reset', reset_handler, 100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()


# Please remember to review the grading rubric

