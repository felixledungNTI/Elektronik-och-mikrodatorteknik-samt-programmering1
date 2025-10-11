import pygame

screen = pygame.display.set_mode((400, 400))
screen.fill((255,0,0))

player = pygame.image.load('assets/flappyBirdPlayer.png')
player = pygame.transform.scale(player, (180,180))
player_rect = player.get_rect()
player_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
        
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
        
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
        
    screen.fill((0, 0, 0))
    screen.blit(player, player_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
pygame.quit()