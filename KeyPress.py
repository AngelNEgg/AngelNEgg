# Key Input Test

import simplegui

message = "Welcome!"
color = "_"
state = "still"

# Handler for scene
def draw(canvas):
    canvas.draw_circle(())

# Handler for keydown
def keydown(key):
    global message
    global state
    ####### Add KEY_MAP to translate to key codes
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
        state = "moved"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"
        state = "moved"
    elif key == simplegui.KEY_MAP["left"]:
        message = "Left arrow"
        state = "moved"
    elif key == simplegui.KEY_MAP["right"]:
        message = "Right arrow"
        state = "moved"
        
frame = simplegui.create_frame("Home", 600, 600)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Start the frame animation
frame.start()
