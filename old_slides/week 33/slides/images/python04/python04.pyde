def drawSeaweed(x, height):
    fill(84, 217, 84)
    for i in range(height):
        ellipse(x, 345-i*20, 10, 25)

def drawSeaweeds():
    randomSeed(45)
    for i in range(15):
        drawSeaweed(5+ i*30, int(random(5)))

def drawStones():
    fill(88, 42, 26)
    ellipse(320,360, 30, 20)
    fill(102, 62, 50)
    ellipse(300,370, 30, 20)
    fill(122, 85, 70)
    ellipse(340,365, 20, 15)

def drawSand():
    fill(255, 199, 135)
    rect(0, 350, 400, 200)

def drawSandcastle(x,y):
    fill(255, 184, 102)
    rect(x+60, y+10, 60, 105)
    rect(x+60, y, 10, 15)
    rect(x+85, y, 10, 15)
    rect(x+110, y, 10, 15)
    rect(x, y+45, 60, 70)
    rect(x+120, y+45, 60, 70)
    rect(x, y+30, 10, 15)
    rect(x+25, y+30, 10, 15)
    rect(x+47, y+30, 10, 15)
    rect(x+170, y+30, 10, 15)
    rect(x+145, y+30, 10, 15)
    rect(x+122, y+30, 10, 15)
    
    fill(204, 147, 78)
    arc(x+90, y+115, 60, 100, PI, TWO_PI)

def drawBackgroundElements():
    background(61, 213, 255)
    drawSand()
    drawSeaweeds()
    drawStones()
    drawSandcastle(22,255)

def drawFish(centerX, centerY, bodyLength, bodyHeight, bodyColor):
    noStroke()
    fill(bodyColor)

    ellipse(centerX, centerY, bodyLength, bodyHeight)
    tailWidth = bodyLength/4
    tailHeight = bodyHeight/2

    triangle(centerX-bodyLength/2, centerY,
             centerX-bodyLength/2-tailWidth, centerY-tailHeight,
             centerX-bodyLength/2-tailWidth, centerY+tailHeight)

    fill(0, 0, 0)
    ellipse(centerX+bodyLength/4, centerY, bodyHeight/5, bodyHeight/5)

def drawBubble(centerX, centerY, radius):
    fill(255, 255, 255)
    ellipse(centerX, centerY, radius, radius)

def setup():
    size(400, 400)
    noStroke()

def draw():
    drawBackgroundElements()
    drawFish(100, 150, 115, 70, color(69, 131, 255))      
    drawFish(283, 284 , -90, 60, color(252, 83, 83))


    drawBubble(175, 130, 17)
    drawBubble(180, 105, 12)
    drawBubble(170, 84, 10)
    drawBubble(225, 255, 15)
    drawBubble(235, 225, 10)
    drawBubble(230, 200, 7)
