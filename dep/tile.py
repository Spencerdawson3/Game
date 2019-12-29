from cnst import *
import random
import pygame
tile_data = {  # name, type, texture
    -1 : ["Ground", -1, pygame.image.load('Textures/ground.png')],
    0 : ["Dirt", 0, pygame.image.load('Textures/dirt.png')],
    1 : ["Grass", 0, pygame.image.load('Textures/grass.png')],
    2 : ["Water", 0, pygame.image.load('Textures/water.png')],
    3 : ["Coal Ore", 0, pygame.image.load('Textures/coal.png')],
    4 : ["Stone", 0, pygame.image.load('Textures/stone.png')],
    5 : ["Lava", 0, pygame.image.load('Textures/lava.png')],
    6 : ["Log", 1, pygame.image.load('Textures/log.png')],
            }


class Tile:

    def __init__(self, in_id):
        self.id = in_id
        self.data = tile_data[self.id]
        self.name = self.data[0]
        self.type = self.data[1]
        self.texture = self.data[2]

    def change_tile(self, new_id):
        self.id = new_id
        self.data = tile_data[self.id]
        self.name = self.data[0]
        self.type = self.data[1]
        self.texture = self.data[2]

        return self

    def drop(self):
        if self.id == GRASS:
            return self.change_tile(DIRT)
        else:
            return self

    # def update(self, adj_tiles):
    #     if self.id == cnst.DIRT:
    #         for tile in adj_tiles:
    #             if tile.id == cnst.GRASS:
    #                 rand_number = random.randrange(1, 3)
    #                 if rand_number == 1:
    #                     self.change_tile(cnst.GRASS)
