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
        #   Get mouse postion as a tuple
        mx, my = pygame.mouse.get_pos()
        #   Set 'y' to original value to avoid moving up and down
        if (mx >= 655):     self.x = 655
        else:   self.x = mx           
        self.y = paddley
        pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
        
    
class Ball:
    def __init__(self, ballx, bally):
        self.ballx = ballx
        self.bally = bally


#   Creating paddle object
paddle = Paddle(paddlex, paddley)

while (running):
    win.fill((0, 0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False
    paddle.createRectangle()
    pygame.display.update()