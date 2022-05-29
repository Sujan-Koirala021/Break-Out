from turtle import width
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

ball_speedX = 10
ball_speedY = 5

running = True
paddlex, paddley  = WIDTH/2-20, HEIGHT -70
ballx, bally = 400, 300
class Paddle:
    width, height = 140, 15
    def __init__(self, paddlex, paddley):
        self.x = paddlex
        self.y = paddley
        
    def createPaddle(self):
        #   Get mouse postion as a tuple
        mx, my = pygame.mouse.get_pos()
        #   Set 'y' to original value to avoid moving up and down
        if (mx >= 655):     self.x = 655
        else:   self.x = mx           
        self.y = paddley
        pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
        

class Ball:
    height = 10
    width = 10
    def __init__(self, x,y , velocityX, velocityY):
        self.x = x
        self.y = y
        self.velx= velocityX
        self.vely = velocityY
    def createBall(self):
        pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
        self.ball_bouncing_mechanism()
        self.moveBall()
        
    def moveBall(self):
        self.x += self.velx
        self.y += self.vely
    
    def ball_bouncing_mechanism(self):
        if self.x <= 0:
            self.velx *= -1
        if self.x >= WIDTH - 10:
            self.velx *= -1
        if self.y <=5 :
            self.vely *= -1
        if self.y >= HEIGHT - 10:
            self.vely *= -1
#   Creating paddle object
paddle = Paddle(paddlex, paddley)
#   Creating ball
ball = Ball(ballx, bally, ball_speedX, ball_speedY)

while (running):
    win.fill((0, 0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False
    paddle.createPaddle()
    ball.createBall()
    pygame.display.update()