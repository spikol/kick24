# States for our FSM
STATE_ON = "ON"
STATE_OFF = "OFF"

# Initial state
current_state = STATE_OFF

def setup():
    size(200, 200)
    fill(255)

def draw():
    background(200)
    
    if current_state == STATE_ON:
        fill(0, 255, 0)  # Green for ON
    elif current_state == STATE_OFF:
        fill(255, 0, 0)  # Red for OFF
    
    ellipse(width/2, height/2, 100, 100)

def mousePressed():
    global current_state
    if current_state == STATE_OFF:
        current_state = STATE_ON
    elif current_state == STATE_ON:
        current_state = STATE_OFF
