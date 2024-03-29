# All complex grahics objects will be stored here

import os
import pygame

class TextureLoader():
    def __init__(self):
        self.data = {}

        potentialTextures = os.listdir("res/gfx")
        
        # Load all scanned textures
        for item in potentialTextures:
            name = item.split('.')[0]
            self.data[name] = pygame.image.load("res/gfx/" + item).convert()
