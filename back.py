import pygame

pygame.init()

size = (1200,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg_w, bg_h = size 
bg = pygame.transform.smoothscale(pygame.image.load('images/space.jpg'), (bg_w, bg_h))
pos_y = 0
speed = 10

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #allKeys = pygame.key.get_pressed()
    pos_y += speed #if allKeys[pygame.K_SPACE] else -speed if allKeys[pygame.K_RIGHT] else 0

    y_rel = pos_y % bg_h
    if y_rel > 0:
        y_part2 = y_rel - bg_h
    else:
        y_rel + bg_h

    screen.blit(bg, (0, y_rel))
    screen.blit(bg, (0, y_part2))

    pygame.display.flip()