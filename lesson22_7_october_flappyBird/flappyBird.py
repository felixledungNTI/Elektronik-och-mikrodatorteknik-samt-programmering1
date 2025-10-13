import pygame
import os

script_dir = os.path.dirname(__file__)
player_path = os.path.join(script_dir, 'assets', 'flappyBirdPlayer.png')
player = pygame.image.load(player_path)
player = pygame.transform.scale(player, (180,180))

pipe_path = os.path.join(script_dir, 'assets', 'flappyBirdPipe.png')
pipe = pygame.image.load(pipe_path)
pipe = pygame.transform.scale(pipe, (180,180))

screen = pygame.display.set_mode((400, 400))
player_rect = player.get_rect()
player_speed = 5

screen.fill((0,0,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    
    screen.fill((0,255,255))
    screen.blit(player,player_rect)
    
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
        
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
        
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
        
    if keys[pygame.K_s]:
        player_rect.y += player_speed
                
    player_rect.x += 1
        
        
    pipe_rect = pipe.get_rect()
    pipe_rect.x = 400
    pipe_rect.y = 0
    screen.blit(pipe, pipe_rect)
    
    if pipe_rect.x < -180:
        pipe_rect.x = 400
        
    if player_rect.colliderect(pipe_rect):
        print('Game Over')
        
    screen.blit(player, player_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
pygame.quit()