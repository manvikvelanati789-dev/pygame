from pygame import *

init()
s = display.set_mode((400, 400))
s.fill("white")
draw.circle(s, "green", (300,300), 50)
draw.circle(s, "green", (100,100), 50, 3)
display.flip()

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
