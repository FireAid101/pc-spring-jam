# Island generation code is here
# Written by FireAid

# We will use regular cellular automata to generate the big island first
import pygame

class Island:
    def __init__(self, width, height):
        self.grid = []
        self.width = width
        self.height = height

        for y in range(0, height):
            temp = []
            for x in range(0, width):
                temp.append('#')

            self.grid.append(temp)

    def draw(self, screen):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] == '#':
                    pos = pygame.Rect(x * 10 + x, y * 10 + y, 10, 10)
                    pygame.draw.rect(screen, "green", pos)

