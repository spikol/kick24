# Declariations
loc_x=200
loc_y=200
size_x=150
size_y=150


def setup():
    size(400, 400) #Size of the window


def draw():
    global loc_x, loc_y, size_x, size_y
    background(255)  # Clear the screen each frame
    draw_cyclops(size_x, size_y,loc_x,loc_y)


def draw_cyclops(loc_x,loc_y,size_x, size_y):
    #global loc_x, loc_y, size_x, size_y
    # Face outline as a circle
    ellipse(loc_x, loc_y, size_x, size_x)
   
    #Drawing the single eye of the Cyclops in the middle of the face
    
    fill(255) #white color
    ellipse(loc_x, loc_x, size_x/3, size_y/3) # Eye
    fill(0) # pupuil black color
    ellipse(loc_x,loc_x, size_x/10, size_y/10)
    fill(200) #gray
   
  
    #Drawing the mouth
    line(loc_x-25, loc_y+50, loc_x+25, loc_y+50) #Simple straight mouth
