import random
BLACK = color(0)
WHITE = color(255)

def setup():
    size(1280, 720)
    background(BLACK)
    
def draw():
    x = random.randint(0, width)
    w = random.randint(1, 50)
    c = random.choice([BLACK, WHITE])
    
    fill(c)
    noStroke()
    rect(x, 0, w, height)
