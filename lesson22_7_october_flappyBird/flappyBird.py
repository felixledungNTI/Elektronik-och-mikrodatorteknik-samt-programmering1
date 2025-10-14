import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
screen.fill((255,0,0))

player = pygame.image.load('assets/flappyBirdPlayer.png')
player = pygame.transform.scale(player, (180,180))
clock = pygame.time.Clock()

pipe = pygame.image.load('assets/flappyBirdPipe.png')
pipe_img = pygame.transform.scale(pipe, (80,400))
pipeGap = 180
pipeSpeed = 3
pipeX = 400
pipeHeight = random.randint(150,400)

def drawPipe(x,height):
    btmRect = pipe.get_rect(midtop=(x,height))
    topImg = pygame.transform.flip(pipe,False,True)
    topRect = topImg.get_rect(midbottom=(x,height-pipeGap))
    screen.blit(pipe_img,btmRect)
    screen.blit(topImg,topRect)
    
    return btmRect,topRect

playerSpeed = 5
playerRect = player.get_rect(center=(100,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        playerRect.x -= playerSpeed
        
    if keys[pygame.K_RIGHT]:
        playerRect.x += playerSpeed
    
    if keys[pygame.K_UP]:
        playerRect.y -= playerSpeed
        
    if keys[pygame.K_DOWN]:
        playerRect.y += playerSpeed
        
    screen.fill((18, 188, 219))
    
    pipeX -= pipeSpeed
    
    if pipeX < -80:
        pipeX = 400
        pipeHeight = random.randint(150,400)
        
    drawPipe(pipeX,pipeHeight)
    
    btmRect, topRect = drawPipe(pipeX, pipeHeight)
    
    if playerRect.colliderect(btmRect) or playerRect.colliderect(topRect):
        print('Game over')
        pygame.quit()
        exit()
    
    screen.blit(player, playerRect)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()