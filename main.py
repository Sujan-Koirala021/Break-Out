import pygame
from pygame.locals import *
WIDTH, HEIGHT = 800, 600
CAPTION= "Smash Brick"
white = (255, 255, 255)
def createWindow(w,h, caption): 
    global win
    pygame.init()
    win = pygame.display.set_mode((w, h))
    pygame.display.set_caption(caption)
createWindow(WIDTH, HEIGHT, CAPTION)

running = True
paddlex, paddley  = WIDTH/2-20, HEIGHT -70
class Paddle:
    width, height = 140, 15
    def __init__(self, paddlex, paddley):
        self.x = paddlex
        self.y = paddley
        
    def createRectangle(self):
        pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )

class Ball:
    def __init__(self, ballx, bally):
        self.ballx = ballx
        self.bally = bally


#   Creating paddle object
paddle = Paddle(paddlex, paddley)

while (running):
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    paddle.createRectangle()
    pygame.display.update()