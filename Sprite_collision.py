import pygame,random

pygame.init()
W, H = 500, 400
s = pygame.display.set_mode((W, H))
bg = pygame.transform.scale(pygame.image.load("messi.png"), (W, H))
f = pygame.font.SysFont("Times New Roman", 72)
c = pygame.time.Clock()
p = pygame.Rect(random.randint(0, W-30), random.randint(0, H-20), 30, 20)
e = pygame.Rect(random.randint(0, W-30), random.randint(0, H-20), 30, 20)
win = 0

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_x):
            pygame.quit()
            quit()

    if not win:
        k = pygame.key.get_pressed()
        p.x = max(0, min(p.x + (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * 5, W - 30))
        p.y = max(0, min(p.y + (k[pygame.K_DOWN] - k[pygame.K_UP]) * 5, H - 20))
        if p.colliderect(e):
            win = 1

    s.blit(bg, (0, 0))
    pygame.draw.rect(s, "black", p)
    if not win:
        pygame.draw.rect(s, "red", e)
    else:
       t = f.render("You Win!", 1, "red")
       s.blit(t, ((W - t.get_width()) // 2, (H - t.get_height()) // 2))

    pygame.display.flip()
    c.tick(60)