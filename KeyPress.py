# Key Input Test

import simplegui

message = "Welcome!"
color = "_"

# Handler for keydown
def keydown(key):
    global message
    ####### Add KEY_MAP to translate to key codes
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"
    elif key == simplegui.KEY_MAP["left"]:
        message = "Left arrow"
    elif key == simplegui.KEY_MAP["right"]:
        message = "Right arrow"
        
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)

# Start the frame animation
frame.start()
