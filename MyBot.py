"""
Naive bot
"""
#!/usr/bin/python3
from hlt import (
    Location, Move,
    CARDINALS, STILL, NORTH, WEST, EAST, SOUTH
)
from networking import (
    getInit, sendInit, getFrame, sendFrame
)
from helper import (
    getStrength, getTerritory, getProduction
)

class MySite:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.target = None
        self.path = None
    def move_on(self):
        if self.path == None or self.target == None:
            raise Exception('Unable to move. This site has no path or target')
        old_x = self.x
        old_y = self.y
        next_dir = path.pop(0)
        if next_dir == NORTH:
            self.y = self.y - 1
        elif next_dir == WEST:
            self.x = self.x - 1
        elif next_dir == SOUTH:
            self.y = self.y + 1
        elif next_dir == EAST:
            self.x = self.x + 1
        return Move(Location(old_x, old_y), next_dir)
    def set_obj(self, path, target):
        self.path = path
        self.target = target
    def clear_path(self):
        self.set_obj(None, None)
    def has_id(self, id):
        return self.id == id

def shortest_path(game_map, Location(x, y)):
    """ Return shortest path between to points of a grid in terms of strength cost """
    """ A* implementation here """

# Clear log file
FILE_WRITER = open('log-ANALYTICS.log', 'w')
FILE_WRITER.write('')
FILE_WRITER.close()

# Initialize data
MY_ID, GAME_MAP = getInit()
mySites = {}
mySitesMap = [[-1 for y in range(GAME_MAP.height)] for x in range(GAME_MAP.width)]
mySiteId = 0
for x in range(GAME_MAP.width):
    for y in range(GAME_MAP.height):
        if GAME_MAP.getSite(Location(x, y)).owner == MY_ID:
            path, target = shortest_path(GAME_MAP, Location(x, y))
            mySites[mySiteId] = MySite(mySiteId, x, y)
            mySites[mySiteId].set_obj(path, target)
            mySitesMap[x][y] = mySiteId
            mySiteId += 1

# Let the fun begins
sendInit('zyzo')

while True:
    MOVES = []
    GAME_MAP = getFrame()
    FILE_WRITER = open('log-ANALYTICS.log', 'a')
    ANALYTICS = {'s': 0, 'a': 0, 'm': 0}
    for x in range(GAME_MAP.width):
        for y in range(GAME_MAP.height):
            curLoc = Location(x, y)
            if GAME_MAP.getSite(curLoc).owner == MY_ID:
                myCurrentSite = mySites[mySitesMap[x][y]]
                if mySitesMap[x][y] != -1:
                    ## registered site
                    if GAME_MAP.getSite(myCurrentSite.target).owner == 0:
                        ## objective still vacant, move it
                        MOVES.append(myCurrentSite.move_on())
                        ## update mySitesMap
                        tmp = mySitesMap[x][y]
                        mySitesMap[x][y] = -1
                        mySitesMap[myCurrentSite.x][myCurrentSite.y] = tmp
                    else:
                        ## objective occupied, calculates new objective
                        path, target = shortest_path(GAME_MAP, x, y)
                        mySites[mySitesMap[x][y]].set_obj(path, target)
                        ## then move it
                        MOVES.append(myCurrentSite.move_on())
                        ## update mySitesMap
                        tmp = mySitesMap[x][y]
                        mySitesMap[x][y] = -1
                        mySitesMap[myCurrentSite.x][myCurrentSite.y] = tmp

    FILE_WRITER.write(
        str(ANALYTICS)
        + str(getTerritory(GAME_MAP, MY_ID)) + 't '
        + str(getStrength(GAME_MAP, MY_ID)) + 's '
        + str(getProduction(GAME_MAP, MY_ID)) + 'p '
        + '\n'
    )
    FILE_WRITER.write(
        str([str(move.loc.x) + str(move.loc.y) + str(move.direction) for move in MOVES]) + '\n'
    )
    FILE_WRITER.close()
    sendFrame(MOVES)
