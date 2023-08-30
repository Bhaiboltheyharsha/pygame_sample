import pygame
from pygame.locals import*
pygame.init()
window = pygame.display.set_mode((500,500))
color = (0,0,255)
radius = 10
run = True
positions=[]
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            positions.append(position)
    for position in positions:
        pygame.draw.circle(window,color,position,10)
    pygame.display.update()
