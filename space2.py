import pygame,random,math

pygame.init()
W,H = 800,600
s = pygame.display.set_mode((W,H))
pygame.display.set_caption("Space Shooter")
bg = pygame.image.load("background.jpg")
p = pygame.image.load("player.png")
e = pygame.image.load("enemy.png")
b = pygame.image.load("bullet.png")
pygame.display.set_icon(p)

px,py,dx = 370,380,0
n= 6
ex = [random.randint(0,736) for i in range(n)]
ey = [random.randint(50,150) for i in range(n)]
ed = [4] * n
eyc = [40] * n
bx,by,bs = 0,py,0
score = 0
f = pygame.font.Font("freesansbold.ttf",32)
o = pygame.font.Font("freesansbold.ttf",64)

run = 1
while run:
    s.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            if event.key == pygame.K_RIGHT:
                dx = 5
            if event.key == pygame.K_SPACE and not bs:
                bx,bs = px,1
        if event.type == pygame.KEYUP and event.key in (1073741904,1073741903):
            dx = 0
            
    px = max(0,min(px+dx,736))
    for i in range(n):
        if ey[i] > 340:
            ey = [2000] * n
            s.blit(o.render("GAME OVER",1,"WHITE"),(200,250))
            break
        ex[i] += ed[i]
        if ex[i] <= 0 or ex[i] >= 736:
            ed[i] *= -1
            ey[i] += eyc[i]

        if math.hypot(ex[i]-bx,ey[i]-by) < 27:
            by,bs = py,0
            score += 1
            ex[i],ey[i] = random.randint(0,736),random.randint(50,150)
        s.blit(e,(ex[i],ey[i]))

    if bs:
        s.blit(b,(bx + 16,by + 10))
        by -= 10
        if by <= 0:
            by, bs = py, 0

    s.blit(p,(px,py))
    s.blit(f.render("Score : "+str(score),1,"WHITE"),(10,10))
    pygame.display.update()
