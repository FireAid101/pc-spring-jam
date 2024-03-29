import pygame
import island
import player
import globals

# Very important
SCALE = 4

# Inital setup
pygame.init()

screen = pygame.display.set_mode((1280, 720), (pygame.SCALED | pygame.DOUBLEBUF))
pygame.display.set_caption("ThermoCraft")
clock = pygame.time.Clock()
isDone = False

globals.load_globals()

camera = pygame.Rect(0, 0, 320 * SCALE, 180 * SCALE)
map = island.Island(200, 200)
map.generate()
map.generate_biomes()

# player = player.Player()

while not isDone:
    # Check events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            isDone = True

    # Update here
    # player.update(camera)

    # Draw here 
    screen.fill("black")
    map.draw(screen, SCALE, camera)

    # player.draw(screen, SCALE)

    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())

pygame.quit()