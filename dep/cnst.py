from dep import tile

# constants representing different resources
GROUND = -1
DIRT = 0
GRASS = 1
WATER = 2
COAL_ORE = 3
STONE = 4
LAVA = 5
LOG = 6
MUD = 8
IRON_ORE = 9
GOLD_ORE = 10
DIAMOND_ORE = 11
CRAFTING_TABLE = 12
WOOD = 13

# constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (50, 50, 50)
RED = (255, 30, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# game dimensions
TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 15

default_tile = tile.Tile(GROUND)