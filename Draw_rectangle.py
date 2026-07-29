import pygame

pygame.init()
s = pygame.display.set_mode((400, 300))
while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()
    pygame.draw.rect(s, "blue", (30, 30, 60, 60))
    pygame.display.flip()