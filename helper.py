"""
"""
from hlt import (
    Location
)

def getTerritory(gameMap, userId):
    territory = 0
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            curSite = gameMap.getSite(Location(x, y))
            if curSite.owner == userId:
                territory += 1
    return territory

def getStrength(gameMap, userId):
    strength = 0
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            curSite = gameMap.getSite(Location(x, y))
            if curSite.owner == userId:
                strength += curSite.strength
    return strength

def getProduction(gameMap, userId):
    production = 0
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            curSite = gameMap.getSite(Location(x, y))
            if curSite.owner == userId:
                production += curSite.production
    return production
