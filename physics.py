# Angel Nazaire
# December - Now (UNFINISHED)
# Personal Project
'''Make a platformer using only SimpleGUI and Python's basic functions. '''

import simplegui

# Constants
WIDTH = 600
HEIGHT = 600
PLAYER_SIZE = 20
GRAVITY = 0.15
JUMP_STRENGTH = -6
SPEED = 3.5

# Global variables
player_pos = [WIDTH // 2, HEIGHT - PLAYER_SIZE]
player_vel = [0, 0]
platforms = [[100, 300, 400, 10], [200, 200, 200, 10]]  # x, y, width, height
on_ground = False

# Draw handler
def draw(canvas):
    global player_pos, player_vel, on_ground

    # Draw player
    canvas.draw_circle(player_pos, PLAYER_SIZE, 1, "Blue", "Blue")

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
    if key == simplegui.KEY_MAP["left"]:
        player_vel[0] = -SPEED
    elif key == simplegui.KEY_MAP["right"]:
        player_vel[0] = SPEED
    elif key == simplegui.KEY_MAP["up"] and on_ground:
        player_vel[1] = JUMP_STRENGTH

# Key up handler
def keyup(key):
    global player_vel
    if key in (simplegui.KEY_MAP["left"], simplegui.KEY_MAP["right"]):
        player_vel[0] = 0

# Create frame
frame = simplegui.create_frame("Platformer", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start frame
frame.start()
