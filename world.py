'''
This manages the map (aka world for the game)
'''
from typing import Dict, List, Tuple, Literal, Any

# block where on which the player would start (?)
# -Perhaps the player should fall from the sky to prevent spawning in a block
#  or bellow
BLOCK_SIZE: int = 16
START_POSITION: Tuple[int, int] = (4, 4)
START_WITH: int = 20 # number of tiles to generate in with
TILE_TYPES: Literal = ['ground', 
                       'dirt']


class World:
    name: str
    map: Dict

    def __init__(self):
        '''
        Generate an initial world
        '''
        self.map = self.generate_horizontal(tile='ground',
                                            tiles=START_WITH,
                                            pos=(0, START_POSITION[0]))

    
    def generate_horizontal(self, tile: TILE_TYPES, tiles: int, pos: Tuple[int, int]):
        '''
        tile: str, type of tiles to generate
        tiles: int, number of blocks to generate
        pos: Tuple(int, int), coordinates of first block to place
        '''
        x, y = pos
        map = {}
        for i in range(tiles):
            map[(x+i, y)] = tile

        return map

