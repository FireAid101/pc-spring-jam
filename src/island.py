# Island generation code is here
# Written by FireAid

# We will use regular cellular automata to generate the big island first
import pygame
import random

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

    def sim(self, cycles):
        for i in range(cycles):
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

                    # if neighbourCount == 2 or neighbourCount == 3 and self.grid[y][x] == '#':
                    #     self.grid[y][x] = '#'
                    #     next
                    
                    # if neighbourCount > 3 and self.grid[y][x] == '#':
                    #     self.grid[y][x] = '.'
                    #     next

                    # if neighbourCount < 2 and self.grid[y][x] == '#':
                    #     self.grid[y][x] = '.'
                    #     next

                    if neighbourCount == 3 and self.grid[y][x] == '.':
                        self.grid[y][x] = '#'
                        next

    def sim_once(self):
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

                if neighbourCount == 2 or neighbourCount == 3 and self.grid[y][x] == '#':
                    self.grid[y][x] = '#'
                    next
                
                if neighbourCount > 3 and self.grid[y][x] == '#':
                    self.grid[y][x] = '.'
                    next

                if neighbourCount < 2 and self.grid[y][x] == '#':
                    self.grid[y][x] = '.'
                    next

                if neighbourCount == 3 and self.grid[y][x] == '.':
                    self.grid[y][x] = '#'
                    next

    def draw(self, screen, scale):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] == '#':
                    pos = pygame.Rect((x * 2) * scale + (x * scale), (y * 2) * scale + (y * scale), 2 * scale, 2 * scale)
                    pygame.draw.rect(screen, "green", pos)

