import pygame,math,random

pygame.init()

s = pygame.display.set_mode((800,500))
pygame.display.set_caption("Space Game")
pygame.display.set_icon(pygame.image.load("ufo.png"))

#UFO PNG DOWNLOAD

bg = pygame.image.load("background.png") #BACKGROUND PNG DOWNLOAD
p = pygame.image.load("player.png") #PLAYER PNG DOWNLOAD
e = pygame.image.load("enemy.png") #ENEMY PNG DOWNLOAD
b = pygame.image.load("bullet.png") #BULLET PNG DOWNLOAD

font = pygame.font.Font("freesansbold.ttf",32)
over = pygame.font.Font("freesansbold.ttf",64)
px, py, dx = 370, 380, 0
bx, by, dy = 0, 380, "ready"

en = [[random.randint(0,736), random.randint(50,150), 4] for i in range(6)]

run = True
while run:
    s.blit(bg,(0,0))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                dx = -5
            if ev.key == pygame.K_RIGHT:
                dx = 5
            if ev.key == pygame.K_SPACE and state == "ready":
                bx, by, state = px, 380, "fire"

        if ev.type == pygame.KEYUP:
            if ev.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                dx = 0

    px = max(0, min(px + dx, 736))

    for i in en:
        if i[1] > 440:
            for j in en:
                j[1] = 2000
            s.blit(over.render("GAME OVER", 1, (255,255,255)), (200,250))
            break

        i[0] += i[2]
        if i[0] <= 0 or i[0] >= 736:
            i[2] *= -1
            i[1] += 40

        if state == "fire" and math.hypot(i[0] - bx, i[1] - by) < 27:
            score +=1
            state = "ready"
            by = 380
            i[0], i[1] = random.randint(0,736), random.randint(50,150)

        s.blit(e, (i[0], i[1]))

    if state == "fire":
        s.blit(b, (bx + 16, by + 10))
        by -= 10
        if by <= 0:
            state = "ready"
            by = 380

    s.blit(p, (px, py))
    s.blit(font.render("Score: " + str(score), 1, (255,255,255)), (10,10))
    pygame.display.update()

    #END ------- END ------