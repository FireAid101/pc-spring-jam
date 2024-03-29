# Island generation code is here

# We will use regular cellular automata to generate the big island first
import pygame
import random
from enum import Enum

import globals

class Biome(Enum):
    PLAINS = 1
    DESERT = 2
    FOREST = 3
    TUNRDA = 4
    TAIGA = 5

class Island:
    def __init__(self, width, height):
        self.grid = []
        self.biomes = []

        # For water animations
        self.frames = [pygame.Rect(0, 12, 12, 12), pygame.Rect(12, 12, 12, 12)]
        self.currentFrame = 0
        self.water_frames = 0 # Frame timer for animations

        # Surfaces for tiles, one for water to animate seperately and the other for all other tiles
        self.temp_surface = pygame.Surface((12, 12), pygame.SRCALPHA)
        self.water_surface = pygame.Surface((12, 12), pygame.SRCALPHA)

        # Load first frame for the water surface
        self.water_surface = pygame.Surface((12, 12), pygame.SRCALPHA)
        self.water_surface.blit(globals.textures.data["tileset"], (0,0), self.frames[self.currentFrame])
        self.water_surface = pygame.transform.scale_by(self.water_surface, (4, 4))
        self.currentFrame += 1

        # Used to save on performance when rendering tiles, so we don't have to create a entirely new surface for the same texture
        self.last_src = pygame.Rect(0, 0, 0, 0)        

        # Island size in tiles
        self.width = width
        self.height = height

        # Generation of land on a body of water
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

    # Using a modified version of Conway's game of life we run two seperate simulations after each other to generate nice looking islands
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
       
    # Generate biomes via simple random number generator
    def generate_biomes(self):
        for y in range(6):
            biome_row = []

            for x in range(6):
                biome_row.append(Biome(random.randrange(1, 6)))
                
            self.biomes.append(biome_row)


    def draw(self, screen : pygame.surface, scale : int, camera : pygame.Rect):
        for y in range(0, self.height):
            for x in range(0, self.width):
                # Simple occullsion culling
                if x * 12 > camera.x - 12 and x * 12 < camera.right and y * 12 > camera.y - 12 and y * 12 < camera.bottom:
                    # Set src to 
                    src = pygame.Rect(0, 0, 0, 0)
                    self.last_biome_index = 0

                    # Set new tileposition
                    pos = pygame.Rect((x * 12) * scale, (y * 12) * scale, 12 * scale, 12 * scale)

                    # Move depending on camera
                    pos.x -= camera.x * scale
                    pos.y -= camera.y * scale

                    # '#' represents land while '.' represents water, handle each case
                    if self.grid[y][x] == '#':
                        gx = int(x / 34) - 1
                        gy = int(y / 34) - 1
                        match self.biomes[gy][gx]:
                            case Biome.DESERT:
                                src = pygame.Rect(24, 0, 12, 12)    
                            case Biome.PLAINS:
                                src = pygame.Rect(0, 0, 12, 12)
                            case Biome.FOREST:
                                src = pygame.Rect(12, 0, 12, 12)
                            case Biome.TAIGA:
                                src = pygame.Rect(36, 0, 12, 12)
                            case Biome.TUNRDA:
                                src = pygame.Rect(36, 0, 12, 12)

                        # For optimization check to see if we have to generate a new tile texture surface
                        if src != self.last_src:
                            self.temp_surface = pygame.Surface((12, 12), pygame.SRCALPHA)
                            self.temp_surface.blit(globals.textures.data["tileset"], (0,0), src)
                            self.temp_surface = pygame.transform.scale_by(self.temp_surface, (scale, scale))
                            self.last_src = src

                        screen.blit( self.temp_surface, pos)

                    elif self.grid[y][x] == '.': # Exact same speel with the water tiles
                        if self.water_frames >= 60:
                            self.water_surface = pygame.Surface((12, 12), pygame.SRCALPHA)
                            self.water_surface.blit(globals.textures.data["tileset"], (0,0), self.frames[self.currentFrame])
                            self.water_surface = pygame.transform.scale_by(self.water_surface, (scale, scale))

                            if self.currentFrame == 1:
                                self.currentFrame = 0
                            else: 
                                self.currentFrame = 1

                            self.water_frames = 0
                        
                        screen.blit( self.water_surface, pos)

        # Advance frame timer for animation
        self.water_frames += 1



