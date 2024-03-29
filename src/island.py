# Island generation code is here
# Written by FireAid

# We will use regular cellular automata to generate the big island first
import pygame
import random
from enum import Enum

class Biome(Enum):
    PLAINS = 1
    DESERT = 2
    FOREST = 3
    TUNRDA = 4
    TAIGA = 5

class Island:
    def __init__(self, width, height):
        self.grid = []
        self.width = width
        self.height = height

        for y in range(0, height):
            temp = []
            for x in range(0, width):
                if ((x < 5 or x > width - 5) or (y < 5 or y > height - 5)):
                    temp.append('.')
                else:
                    gen_id = random.randrange(0, 101)

                    if gen_id > 89:
                        temp.append('#')
                    else:
                        temp.append('.')

            self.grid.append(temp)

    def generate(self):
        for i in range(20):
            for y in range(5, self.height - 5):
                for x in range(5, self.width - 5): 
                    neighbourCount = 0

                    if self.grid[y][x - 1] == '#': neighbourCount += 1
                    if self.grid[y - 1][x - 1] == '#': neighbourCount += 1
                    if self.grid[y - 1][x + 1] == '#': neighbourCount += 1
                    if self.grid[y][x + 1] == '#': neighbourCount += 1
                    if self.grid[y + 1][x + 1] == '#': neighbourCount += 1
                    if self.grid[y + 1][x] == '#': neighbourCount += 1
                    if self.grid[y + 1][x - 1] == '#': neighbourCount += 1

                    if neighbourCount == 3 and self.grid[y][x] == '.':
                        self.grid[y][x] = '#'
                        next

        for y in range(5, self.height - 5):
            for x in range(5, self.width - 5): 
                neighbourCount = 0

                if self.grid[y][x - 1] == '#': neighbourCount += 1
                if self.grid[y - 1][x - 1] == '#': neighbourCount += 1
                if self.grid[y - 1][x + 1] == '#': neighbourCount += 1
                if self.grid[y][x + 1] == '#': neighbourCount += 1
                if self.grid[y + 1][x + 1] == '#': neighbourCount += 1
                if self.grid[y + 1][x] == '#': neighbourCount += 1
                if self.grid[y + 1][x - 1] == '#': neighbourCount += 1

                if neighbourCount > 3 and self.grid[y][x] == '.':
                    self.grid[y][x] = '#'
                    next

                if neighbourCount < 2 and self.grid[y][x] == '#':
                    self.grid[y][x] = '.'
                    next
       
    def draw(self, screen : pygame.surface, scale : int, camera : pygame.Rect):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] == '#':
                    # Simple occullsion culling
                    if x * 2 > camera.x and x * 2 < camera.right and y * 2 > camera.y and y * 2 < camera.bottom:
                        pos = pygame.Rect((x * 2) * scale, (y * 2) * scale, 2 * scale, 2 * scale)
                        pos.x -= camera.x * scale
                        pos.y -= camera.y * scale
                        pygame.draw.rect(screen, "green", pos)

