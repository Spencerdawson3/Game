import random
from cnst import *
from tile import *


class Chunk:

    def __init__(self):
        # assign coordinates
        self.x = 0
        self.y = 0
        # generate random terrain for chunk
        self.map = [["" for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                self.i = random.randrange(0, 101)
                if 0 <= self.i < 10:
                    self.tile = Tile(DIRT)
                elif 10 <= self.i < 15:
                    self.tile = Tile(WATER)
                elif 15 <= self.i < 20:
                    self.tile = Tile(COAL_ORE)
                elif 20 <= self.i < 25:
                   self.tile = Tile(STONE)
                elif 25 <= self.i < 30:
                    self.tile = Tile(LAVA)
                elif 30 <= self.i < 35:
                    self.tile = Tile(LOG)
                elif 35 <= self.i < 40:
                    self.tile = default_tile
                else:
                    self.tile = Tile(GRASS)

                self.map[rw][cl] = self.tile
