import pygame
import os
import sys
import random

pygame.init()

pygame.mixer.music.load('assets/bgMusic.mp3')
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

script_dir = os.path.dirname(__file__)
player_path = os.path.join(script_dir, 'assets', 'flappyBirdPlayer.png')
player = pygame.image.load(player_path)
player = pygame.transform.scale(player, (180, 180))

pipe_path = os.path.join(script_dir, 'assets', 'flappyBirdPipe.png')
pipe = pygame.image.load(pipe_path)
pipe = pygame.transform.scale(pipe, (180, 180))
topPipeImage = pygame.transform.rotate(pipe, 180)

pygame.display.set_caption('Flappy Bird')

font = pygame.font.SysFont(None, 50)

screen = pygame.display.set_mode((400, 400))
player_rect = player.get_rect()
player_speed = 10

player_rect.x = 100
player_rect.y = 200

playerY = float(player_rect.y)

screen.fill((0, 0, 255))

pipeWidth = 180
pipeHeight = 180
gap = 150

pipeStartX = 800
gap = 150

topPipeRect = pipe.get_rect()
btmPipeRect = pipe.get_rect()


def resetPipe():
    global topPipeRect, btmPipeRect

    topPipeRect.x = pipeStartX
    btmPipeRect.x = pipeStartX

    topPipeRect.y = 0

    minBtmY = topPipeRect.y + pipeHeight + 50
    maxBtmY = 400 - pipeHeight
    btmPipeRect.y = topPipeRect.y + pipeHeight + gap


resetPipe()

clock = pygame.time.Clock()
game_over = False


def checkCollision():
    playerHit = player_rect.inflate(-60,-60)
    topPipeHit = topPipeRect.inflate(-20, -20)
    btmPipeHit = btmPipeRect.inflate(-20, -20)
    
    return playerHit.colliderect(topPipeHit) or playerHit.colliderect(btmPipeHit)


def showGameOver():
    screen.fill((0, 0, 0))
    text = font.render('Game Over', True, (255, 0, 0))
    restartText = font.render('Press R to restart', True, (255, 255, 255))
    screen.blit(text, (100, 180))
    screen.blit(restartText, (50, 220))
    pygame.display.flip()

def restartGame():
    global playerY, game_over
    playerY = 200
    player_rect.y = int(playerY)
    resetPipe()
    game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if not game_over:
        screen.fill((0, 255, 255))

        if keys[pygame.K_UP]:
            playerY -= player_speed

        if keys[pygame.K_DOWN]:
            playerY += player_speed

        if playerY < 0:
            playerY = 0
        if playerY + player_rect.height > 400:
            playerY = 400 - player_rect.height

        player_rect.y = int(playerY)

        topPipeRect.x -= 3
        btmPipeRect.x -= 3

        if topPipeRect.right < 0:
            resetPipe()

        if checkCollision():
            game_over = True

        screen.blit(topPipeImage, topPipeRect)
        screen.blit(pipe, btmPipeRect)

        screen.blit(player, player_rect)

    else:
        showGameOver()
        if keys[pygame.K_r]:
            restartGame()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()