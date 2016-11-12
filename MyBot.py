#!/usr/bin/python3
from hlt import (
    Location, Move,
    CARDINALS, STILL, NORTH, WEST
)
from networking import (
    getInit, sendInit, getFrame, sendFrame, random
)
from helper import (
    getStrength, getTerritory, getProduction
)



sendInit('zyzo')
f = open('log-analytics.log', 'w')
f.write('')
f.close()
roundCnt = 0

"""
STRATEGY
1. Try to occupy unoccupied regions (1 map = 4 equal square regions)
"""

myID, gameMap = getInit()
while True:
    moves = []
    gameMap = getFrame()
    f = open('log-analytics.log', 'a')
    analytics = { 's': 0, 'a': 0, 'm': 0 }
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            curLoc = Location(x, y)
            if gameMap.getSite(curLoc).owner == myID:
                movedPiece = False
                for d in CARDINALS:
                    if (
                        gameMap.getSite(curLoc, d).owner != myID
                        and gameMap.getSite(curLoc, d).strength
                        < gameMap.getSite(curLoc).strength
                    ):
                        moves.append(Move(curLoc, d))
                        analytics['a'] += 1
                        movedPiece = True
                        break
                #if not movedPiece and gameMap.getSite(curLoc).strength == 0:
                if not movedPiece:
                    moves.append(Move(curLoc, STILL))
                    analytics['s'] += 1
                    movedPiece = True
                #if not movedPiece:
                #    moves.append(Move(curLoc, NORTH if bool(int(random.random() * 2)) else WEST))
                #    analytics['m'] += 1
                #    movedPiece = True
    f.write(str(analytics)
        + str(getTerritory(gameMap, myID)) + 't '
        + str(getStrength(gameMap, myID)) + 's '
        + str(getProduction(gameMap, myID)) + 'p '
        + '\n')
    f.write(str([str(move.loc.x) + str(move.loc.y) + str(move.direction) for move in moves]) + '\n')
    f.close()
    sendFrame(moves)
    roundCnt += 1
