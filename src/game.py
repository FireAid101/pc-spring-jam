import pygame
import island

# Very important
SCALE = 4

# Inital setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
clock = pygame.time.Clock()
isDone = False

camera = pygame.Rect(0, 0, 320 * SCALE, 180 * SCALE)
map = island.Island(200, 200)
map.generate()

while not isDone:
    # Check events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            isDone = True

    # Update here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera.y -= 1
    if keys[pygame.K_s]:
        camera.y += 1
    if keys[pygame.K_a]:
        camera.x -= 1
    if keys[pygame.K_d]:
        camera.x += 1

    # Draw here 
    screen.fill("black")
    map.draw(screen, SCALE, camera)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()