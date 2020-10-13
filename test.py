def f(a, b, d):
    c = a + b * d
    print(c)



f(5, 10, 1)
""
import pygame
screen = pygame.display.set_mode((1060, 720))
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False