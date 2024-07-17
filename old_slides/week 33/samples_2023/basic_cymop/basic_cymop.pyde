# Cyclops properties
cyclops_x =200
cyclops_y = 200
cyclops_radius = 50

def setup():
    size(400, 400)
    background(255)

def draw():
    background(255)  # Clear the screen each frame
    # Draw the cyclops
    draw_cyclops(cyclops_x, cyclops_y)

def draw_cyclops(x, y):
    # Head of the cyclops
    fill(200, 200, 250)
    ellipse(x, y, 2 * cyclops_radius, 2 * cyclops_radius)

    # Eye of the cyclops
    fill(255)
    ellipse(x, y-10, cyclops_radius, cyclops_radius)
    
    # Pupil of the cyclops
    fill(0)
    ellipse(x, y-10, cyclops_radius / 4, cyclops_radius / 4)
    
    # Mouth of the cyclops
    line(x-25, y+35, x+25, y+35) # Simple straight mouth
