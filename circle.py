import pgzrun

def draw():
    screen.clear()
    screen.draw.filled_circle((80,80),40,(255,255,0))
    screen.draw.filled_circle((160,80),40,(255,255,0))
    screen.draw.filled_circle((240,80),40,(255,255,0))
    screen.draw.filled_circle((320,80),40,(255,255,0))
    Colors = ('red','green','blue','white')
    for n in range (4):
        screen.draw.filled_circle((200,200), 25*(4-n), Colors[n])

TITLE = "Test Fill circle by pygame Zero"
WIDTH = 400
HEIGHT = 300

pgzrun.go()
