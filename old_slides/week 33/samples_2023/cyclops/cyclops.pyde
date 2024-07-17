# Simple example of drawing

size(400, 400) #Size of the window

# Face outline as a circle
ellipse(200, 200, 150, 150) 

#Drawing the single eye of the Cyclops in the middle of the face
fill(200) #Black color
ellipse(200, 175, 60, 60) # Eye
fill(0)
ellipse(200,175, 20,20)
  
#Drawing the mouth
line(175, 235, 225, 235) #Simple straight mouth
