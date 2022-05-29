import pygame
from pygame.locals import *
WIDTH, HEIGHT = 800, 600
CAPTION= "Smash Brick"

def createWindow(w,h, caption): 
    pygame.init()
    win = pygame.display.set_mode((w, h))
    pygame.display.set_caption(caption)

createWindow(WIDTH, HEIGHT, CAPTION)

running = True

while (running):
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    pygame.display.update()