import random

GRAY_50 = color(127)
BLACK = color(0)
WHITE = color(255)

barcode_colors = [BLACK, GRAY_50, WHITE]

def setup():
    size(1280, 720)
    background(BLACK)
    
def draw():
    x = random.randint(0, width)
    w = random.randint(1, 50)
    c = random.choice(barcode_colors)
    
    fill(c)
    noStroke()
    rect(x, 0, w, height)
