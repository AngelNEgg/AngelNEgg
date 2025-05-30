# Angel Nazaire
# December - Now (UNFINISHED)
# Personal Project
'''Make a platformer using only SimpleGUI and Python's basic functions. '''

import simplegui

# Constants
WIDTH = 600
HEIGHT = 400
PLAYER_SIZE = 10
GRAVITY = .2
JUMP_STRENGTH = -6
SPEED = 4.5

# Global variables
player_pos = [WIDTH // 2, HEIGHT - PLAYER_SIZE]
player_vel = [0, 0]
platforms = [[100, 350, 150, 10], [390, 220, 200, 10],[160,150,150,10],[200,285,150,10]]  # x, y, width, height
on_ground = False

# Draw handler
def draw(canvas):
    global player_pos, player_vel, on_ground

    # Draw player
    canvas.draw_circle(player_pos, PLAYER_SIZE, 3, "Navy", "Blue")

    # Draw platforms
    for platform in platforms:
        canvas.draw_polygon(
            [
                (platform[0], platform[1]),
                (platform[0] + platform[2], platform[1]),
                (platform[0] + platform[2], platform[1] + platform[3]),
                (platform[0], platform[1] + platform[3]),
            ],
            1,
            "Green",
            "Green",
        )

    # Update player position
    player_vel[1] += GRAVITY
    player_pos[0] += player_vel[0]
    player_pos[1] += player_vel[1]

    # Check for ground collision
    if player_pos[1] + PLAYER_SIZE > HEIGHT:
        player_pos[1] = HEIGHT - PLAYER_SIZE
        player_vel[1] = 0
        on_ground = True
    else:
        on_ground = False

    # Check for platform collision
    for platform in platforms:
        if (
            platform[0] <= player_pos[0] <= platform[0] + platform[2]
            and player_pos[1] + PLAYER_SIZE >= platform[1]
            and player_pos[1] + PLAYER_SIZE <= platform[1] + platform[3] + 5
        ):
            player_pos[1] = platform[1] - PLAYER_SIZE
            player_vel[1] = 0
            on_ground = True

# Key down handler
def keydown(key):
    global player_vel
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["A"]:
        player_vel[0] = -SPEED
    elif key == simplegui.KEY_MAP["right"] or key == simplegui.KEY_MAP["D"]:
        player_vel[0] = SPEED
    elif (key == simplegui.KEY_MAP["up"] and on_ground) or (key == simplegui.KEY_MAP["W"] and on_ground) or (key == simplegui.KEY_MAP["space"] and on_ground):
        player_vel[1] = JUMP_STRENGTH

# Key up handler
def keyup(key):
    global player_vel
    if key in (simplegui.KEY_MAP["left"], simplegui.KEY_MAP["right"]):
        player_vel[0] = 0
    elif key in (simplegui.KEY_MAP["A"], simplegui.KEY_MAP["D"]):
        player_vel[0] = 0

# Create frame
frame = simplegui.create_frame("Platformer", WIDTH, HEIGHT)
frame.set_canvas_background("#a1e9ff")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start frame
frame.start()
