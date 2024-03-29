import pygame
import island

# Very important
SCALE = 4

# Inital setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
clock = pygame.time.Clock()
isDone = False

camera = [0, 0, 320, 180]
map = island.Island(50, 50)
map.sim(2)
map.sim_once()

while not isDone:
    # Check events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            isDone = True

    # Update here

    # Draw here 
    screen.fill("black")
    map.draw(screen, SCALE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()