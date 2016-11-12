"""
"""
from hlt import (
    Location,
    NORTH, WEST, EAST, SOUTH
)

def getTerritory(gameMap, myID, region = None):
    territory = 0
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            curSite = gameMap.getSite(Location(x, y))
            if curSite.owner != myID and curSite.owner != 0:
                territory += curSite.strength
    return territory
