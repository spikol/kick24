# Declariations
x=200
y=200

def setup():
    size(400, 400) #Size of the window
    print(x)


def draw():
    background(200)  # Clear the screen each frame
    draw_cyclops(x, y)
    draw_cyclops(x-125, y-125)


def draw_cyclops(x, y):
    # Face outline as a circle
    ellipse(x, y, 150, 150) 

    #Drawing the single eye of the Cyclops in the middle of the face
    fill(200) #Black color
    ellipse(x, y-25, 60, 60) # Eye
    fill(0)
    ellipse(x, y-25, 20,20)
    fill(255)
  
    #Drawing the mouth
    #line(175, 235, 225, 235) #Simple straight mouth
    line(x-25,y+35, x+25, y+35)
