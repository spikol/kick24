## Variables Declaration
x = 100

## The Stage
def setup():
    size(400, 400)
    noStroke()

## Main Loop
def draw():
    global x
    drawEverything()
    x+=1

## My Custom Functions

def drawEverything(): ## My Main Function
    drawScene() # draws the scene
    drawFish(x, 140, 15)
    drawStones(300)
    drawSeaweed(65)

def drawFish(fishX, fishY, eyeSize):
    # Krop
    fill(255, 157, 0)
    ellipse(fishX, fishY, 120, 75)
    
    # Finner
    fill(247, 222, 0)
    triangle(fishX-60, fishY, fishX-90, fishY-30, fishX-90, fishY+30)
    triangle(fishX+10, fishY+10, fishX-20, fishY, fishX-20, fishY+25)

    # Øje
    fill(0, 0, 0)
    ellipse(fishX + 30, fishY-10, eyeSize, eyeSize)
    fill(255, 255, 255)
    ellipse(fishX + 32, fishY-10, 5, 5)

def drawStones(stonesX):
    fill(88, 42, 26)
    ellipse(stonesX + 20, 360, 30, 20)
    fill(102, 62, 50)

def drawSeaweed(seaweedX):
    fill(84, 217, 84)
    ellipse(seaweedX - 15, 345, 10, 25)
    ellipse(seaweedX - 15, 325, 10, 25)
    ellipse(seaweedX - 15, 305, 10, 25)
    ellipse(seaweedX, 345, 10, 25)

def drawScene():
    # Vand
    background(61, 213, 255)
    fill(255, 199, 135)
    # Sand
    rect(0, 350, 400, 200)


    
    
