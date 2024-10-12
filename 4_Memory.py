# implementation of card game - Memory

import simplegui
import random

#lis = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0]
lis = range(8)
lis.extend(range(8))

face_up = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
card1 = 0
card2 = 0
state = 0
count = 0

random.shuffle(lis)

# helper function to initialize globals
def new_game():
    global state, count, face_up
    random.shuffle(lis)
    face_up = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    state = 0
    count = 0
    label.set_text("Turns = " + str(count))

     
# define event handlers
def mouseclick(pos):
    global card1, card2, state, count
    card_num = pos[0] // 50
    
    if state == 0 :
        state = 1
        count += 1
        card1 = card_num
        face_up[card_num] = True
    elif state == 1 :
        if face_up[card_num] == False :
            state = 2
            card2 = card_num
            face_up[card_num] = True
    elif state == 2 :
        if face_up[card_num] == False :
            state = 1
            if lis[card1] != lis[card2] :
                face_up[card1] = False 
                face_up[card2] = False 
            card1 = card_num
            face_up[card_num] = True
            count += 1
            
    label.set_text("Turns = " + str(count))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16) :
        if face_up[i] == False :
            canvas.draw_line([50 * i + 25,0], [50 * i + 25,100], 48, "green")
        else :
            canvas.draw_text(str(lis[i]), [50 * i + 15, 70], 40, "white")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubrics