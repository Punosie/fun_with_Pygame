import pygame

#Setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('Black')

    pygame.draw.circle(screen, 'pink', player_pos, player_radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


#Boundary
    
    if player_pos.x - player_radius < 0:
        player_pos.x = player_radius
    elif player_pos.x + player_radius > screen_width:
        player_pos.x = screen_width - player_radius

    if player_pos.y - player_radius < 0:
        player_pos.y = player_radius
    elif player_pos.y + player_radius > screen_height:
        player_pos.y = screen_height - player_radius

    pygame.display.flip()

    dt = clock.tick(60)/1000


pygame.quit()