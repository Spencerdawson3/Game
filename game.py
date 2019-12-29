# import the pygame module, and the
# sys module for exiting the window
import pygame
import sys

# import random
print(sys.path)
from dep import chunk
from dep.cnst import *
from dep import inv
# import some useful constants
from pygame.locals import *

inventory = [inv.Slot() for i in range(11)]
# player and location info
PLAYER = pygame.image.load('Textures/player.png')
playerpos = [0, 0]
playerchunkx = 0
playerchunky = 0

# tilemap list
startchunk = chunk.Chunk()
startchunk.coordinates = [0, 0]
chunks = [startchunk]


def update_chunk(playerchunkcoord):
    # check if a chunk exists at these coordinates
    for item in chunks:
        # print(str(item.coordinates) + " chunk being compared to player coordinates")
        if item.x == playerchunkcoord[0] and item.y == playerchunkcoord[1]:
            return item

    # if not, make a new one
    new_chunk = chunk.Chunk()
    new_chunk.x = playerchunkcoord[0]
    new_chunk.y = playerchunkcoord[1]
    chunks.append(new_chunk)
    return new_chunk


def add_to_inventory(tile):
    # if a slot already exists with this tile, add to it

    for item in inventory:
        if not len(item.tile) == 0:
            if item.tile[0].id == tile.id and len(item.tile) < item.MAX:
                item.tile.append(tile)
                return True

    for item in inventory:
        if len(item.tile) == 0:
            item.tile.append(tile)
            return True
    print("false")
    return False


# initialise the pygame module
pygame.init()

# create a new drawing surface, width=300, height=300
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 60))
# give the window a caption
pygame.display.set_caption('Game')

INVFONT = pygame.font.Font('freesansbold.ttf', 18)
INFOFONT = pygame.font.Font('freesansbold.ttf', 14)
# get tilemap from chunk
tilemap = update_chunk([playerchunkx, playerchunky])

clock = pygame.time.Clock()
mouse_coordinates = (0, 0)
# loop forever
while True:
    # get mouse position and relative tile
    mouse_pos = pygame.mouse.get_pos()
    mouse_coordinates = [0, 0]
    if MAPHEIGHT * TILESIZE - 1 >= mouse_pos[1] and mouse_pos[0] <= MAPWIDTH * TILESIZE:
        mouse_coordinates = ((mouse_pos[1] - (mouse_pos[1] % TILESIZE)) / TILESIZE,
                             (mouse_pos[0] - (mouse_pos[0] % TILESIZE)) / TILESIZE)
    # get all the user events
    for event in pygame.event.get():
        # placement keys
        placekey = {
            K_1: inventory[0],
            K_2: inventory[1],
            K_3: inventory[2],
            K_4: inventory[3],
            K_5: inventory[4],
            K_6: inventory[5],
            K_7: inventory[6],
            K_8: inventory[7],
            K_9: inventory[8],
            K_0: inventory[9]
        }

        # if the user wants to quit
        if event.type == QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()

        # controls
        elif event.type == KEYDOWN:

            # movement controls
            if event.key == K_d:
                if playerpos[0] < MAPWIDTH - 1:
                    # if tilemap.map[playerpos[1]][playerpos[0] + 1].type != 1:
                    # playerpos[0] += 1
                    playerpos[0] += 1
                else:
                    playerchunkx += 1
                    playerpos[0] = 0

            elif event.key == K_a:
                if playerpos[0] > 0:
                    playerpos[0] -= 1
                else:
                    playerchunkx -= 1
                    playerpos[0] = MAPWIDTH - 1

            elif event.key == K_s:
                if playerpos[1] < MAPHEIGHT - 1:
                    playerpos[1] += 1
                else:
                    playerchunky += 1
                    playerpos[1] = 0

            elif event.key == K_w:
                if playerpos[1] > 0:
                    playerpos[1] -= 1
                else:
                    playerchunky -= 1
                    playerpos[1] = MAPHEIGHT - 1

            # update tilemap
            tilemap = update_chunk([playerchunkx, playerchunky])

            # store tile being stood on
            cur_tile = tilemap.map[playerpos[1]][playerpos[0]]
            print(cur_tile.name)

            # mine control
            # if not cur_tile == GROUND:
            if not cur_tile.id == GROUND:
                if event.key == K_SPACE:
                    if add_to_inventory(cur_tile.drop()):
                        cur_tile = default_tile

            # placement controls
            if cur_tile.name == "Ground":
                # if the pressed key is a valid place key, store the item selected
                if event.key in placekey:
                    selected_slot = placekey[event.key]

                    # look for the inventory slot
                    if not len(selected_slot.tile) == 0:
                        cur_tile = selected_slot.tile.pop()
                    if len(selected_slot.tile) == 0:
                        inventory.append(inventory.pop(inventory.index(selected_slot)))
                        # for item in inventory:
                        #     index += 1
                        #     # if the slot is found and it is a tile reduce the amount by one and place it on the tilemap
                        #     if item == selected_slot and len(item.tile) > 0:
                        #         cur_tile = selected_slot.tile.pop()
                        #         # if there is no more tiles in the slot change the tile type to -1 and shift the slots
                        #         if len(item.tile) == 0:
                        #             inventory.append(inventory.pop(index))

            # replace tile being stood on
            tilemap.map[playerpos[1]][playerpos[0]] = cur_tile

        elif event.type == MOUSEBUTTONDOWN:
            print(mouse_pos)
            print(mouse_coordinates)

    # TEST FOR EVENTS
    # print(str(event))
    # TEST FOR PLAYER POSITION
    # print(tilemap.map[playerpos[1]][playerpos[0]])

    # display background
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, MAPHEIGHT * TILESIZE, MAPWIDTH * TILESIZE, 80))
    # display tilemap
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(tilemap.map[row][column].texture, (column * TILESIZE, row * TILESIZE))
            DISPLAYSURF.blit(PLAYER, (playerpos[0] * TILESIZE, playerpos[1] * TILESIZE))

    # highlight tile under cursor
    tile_top_left = (mouse_coordinates[1] * TILESIZE, mouse_coordinates[0] * TILESIZE)
    tile_top_right = (mouse_coordinates[1] * TILESIZE + 39, mouse_coordinates[0] * TILESIZE)
    tile_bottom_left = (mouse_coordinates[1] * TILESIZE, mouse_coordinates[0] * TILESIZE + 39)
    tile_bottom_right = (mouse_coordinates[1] * TILESIZE + 39, mouse_coordinates[0] * TILESIZE + 39)
    pygame.draw.lines(DISPLAYSURF, WHITE, True, (tile_bottom_left, tile_bottom_right, tile_top_right, tile_top_left), 3)

    # display the inventory
    inv_place_position = 10
    for item in inventory:
        if len(item.tile) > 0 and inv_place_position < (MAPWIDTH * TILESIZE) - 120:
            # display resource image
            DISPLAYSURF.blit(item.tile[0].texture, (inv_place_position, MAPHEIGHT * TILESIZE + 10))
            # add counter text
            text_obj = INVFONT.render(str(len(item.tile)), True, WHITE)
            DISPLAYSURF.blit(text_obj, (inv_place_position, MAPHEIGHT * TILESIZE + 10))
            inv_place_position += 50

    # display information about object under cursor
    mouse_tile = tilemap.map[int(mouse_coordinates[0])][int(mouse_coordinates[1])]
    mouse_tile_data = [str(mouse_tile.name), str(mouse_tile.id)]
    mouse_place_position = 5
    for item in mouse_tile_data:
        text_obj = INFOFONT.render(item, True, WHITE)
        DISPLAYSURF.blit(text_obj, (MAPWIDTH * TILESIZE - 80, MAPHEIGHT * TILESIZE + mouse_place_position))
        mouse_place_position += 15
    # update the display
    pygame.display.update()
    clock.tick(60)
