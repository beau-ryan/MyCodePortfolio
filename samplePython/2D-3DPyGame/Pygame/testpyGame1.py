## test module as I feel like creating 

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("welcome to test1")

res = 720, 480
screen = pygame.display.set_mode(res)
color = (0, 0, 0 )
surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
surface.fill(color)


# Game Loop
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            print("success") 
            raise SystemExit
        else:
            if ev.type == pygame.event.get():
                ev.type ==pygame.display.update
                running = False
                print("Error")
                raise SystemError
                
            
pygame.display.flip()   

pygame.quit()
