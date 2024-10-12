# template for "Stopwatch: The Game"

import simplegui

# define global variables
msec = 0
attempt = 0
success = 0
run = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tsec = t / 10 
    min = tsec / 60
    sec = tsec % 60
    minsec = t % 10
    if sec < 10 :
        return str(min) + ":0" + str(sec) + "." +str(minsec)
    else :
        return str(min) + ":" + str(sec) + "." + str(minsec)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start() :
    global run 
    run = True 
    timer.start()
    
def stop() :
    global attempt, success, run, msec
    timer.stop()
    if run:
        if msec % 10 == 0:
            success += 1
            attempt += 1
        else :
            attempt += 1
    run = False

    
def reset():
    global attempt, success, run, msec 
    attempt = 0
    success = 0
    msec = 0
    run = False 
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global msec
    msec += 1

# define draw handler
def draw_handler(canvas):
    global msec, attempt, success
    s = format(msec)
    s2 = str(success) + "/" + str(attempt)
    canvas.draw_text(s, [40,115], 50, "white")
    canvas.draw_text(s2, [160, 20] , 20, "green")
    
# create frame
frame = simplegui.create_frame("stopwatch", 200, 200)
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw_handler)


# register event handlers
button1 = frame.add_button("Start", start)
button2 = frame.add_button("Stop", stop)
button3 = frame.add_button("Reset", reset)

# start frame
frame.start()

# Please remember to review the grading rubric
