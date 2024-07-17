# States for our FSM
STATE_RED = "RED"
STATE_GREEN = "GREEN"

# Initial state
current_state = STATE_RED

def setup():
    size(200, 200)
    fill(255)

def draw():
    background(200)
    
    if current_state == STATE_RED:
        fill(255, 0, 0)  # Red color for RED state
    elif current_state == STATE_GREEN:
        fill(0, 255, 0)  # Green color for GREEN state
    
    ellipse(width/2, height/2, 100, 100)

def mousePressed():
    global current_state
    if current_state == STATE_RED:
        current_state = STATE_GREEN
    elif current_state == STATE_GREEN:
        current_state = STATE_RED