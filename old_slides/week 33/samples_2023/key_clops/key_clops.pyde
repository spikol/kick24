# Cyclops properties
cyclops_x = 200
cyclops_y = 200
cyclops_radius = 50
cyclops_speed = 5

# Stage 

def setup():
    size(800, 600)
    background(255)
    
## Main Loop
def draw():
    global cyclops_y
    global cyclops_x
    global cyclops_speed
    background(205)  # Clear the screen each frame

    # # Check which keys are pressed and update cyclops position 
    # Conditional statement
    if keyPressed:
        if key == 'Q' or key == 'q':
            cyclops_y -= cyclops_speed
        elif key == 'A' or key == 'a':
            cyclops_y += cyclops_speed
        elif key == 'O' or key == 'o':
            cyclops_x -= cyclops_speed
        elif key == 'P' or key == 'p':
            cyclops_x += cyclops_speed

    # Draw the cyclops call the function
    draw_cyclops(cyclops_x, cyclops_y)

# Functions
def draw_cyclops(x, y):
    # Head of the cyclops
    fill(200, 200, 250)
    ellipse(x, y, 2 * cyclops_radius, 2 * cyclops_radius)

    # Eye of the cyclops
    fill(255)
    ellipse(x, y, cyclops_radius, cyclops_radius)
    
    # Pupil of the cyclops
    fill(0)
    ellipse(x, y, cyclops_radius / 3, cyclops_radius / 3)
