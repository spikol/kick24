#variable postion for x 
x_pos = 0

#set up
def setup():
    size (400 , 400)
    

#main loop
def draw(): 
    global x_pos #variable comment out and see what happens
    background (240) #sets the color used for the background of the stage
    ellipse(x_pos, height/2, 50, 50) 
    x_pos += 2 #
    # Conditional to check if the circle is out of bounds
    if x_pos > width: x_pos = 0
