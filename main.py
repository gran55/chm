import pygame
import random

num = random.randint(0,1000)
print (num)
W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Сколько у тебя IQ?")
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False