import pgzrun

def draw():
    screen.fill((0, 255, 191))
    screen.draw.text("Hello World", topleft = (10,10), fontsize = 30)

TITLE = "Hello World By Pygame Zero"
WIDTH = 400
HEIGHT = 300

pgzrun.go()
