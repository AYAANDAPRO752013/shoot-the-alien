import pgzrun
from random import randint

WIDTH=600
HEIGHT=500
TITLE="Shoot The Alien"

message="lets start"
alien=Actor("alien")
#alien.pos=(50,50)

def draw():
    screen.clear()
    screen.fill(color=(225,225,225))
    #place_alien()
    alien.draw()
    screen.draw.text(message,center=(500,10),fontsize=30)

def place_alien():
    alien.x=randint(50,WIDTH-50)
    alien.y=randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="GUUUUD BOY!!"
        place_alien()
    else:
        message="BAAAAD BOY!!"
        

    
    
pgzrun.go()
