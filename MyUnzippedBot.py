#!/usr/bin/python3
from hlt import (
    Location, Move,
    CARDINALS, STILL, NORTH, WEST
)
from networking import (
    getInit, sendInit, getFrame, sendFrame, random
)
from helper import (
    getTerritory
)

"""
STRATEGY
1. Try to occupy unoccupied regions (1 map = 4 equal square regions)
2. In the beginning it's easy to get stuck. Sole objective is to occupy new sites (kickstart phase)
"""

myID, gameMap = getInit()
sendInit('zyzo')
f = open('logfile.log', 'w')
f.write('')
f.close()
roundCnt = 0
while True:
    moves = []
    gameMap = getFrame()
    f = open('logfile.log', 'a')
    analytics = { 's': 0, 'a': 0, 'e': 0, 'm': 0 }
    if roundCnt < 25:
        # kickstart
        for y in range(gameMap.height):
            for x in range(gameMap.width):
                curLoc = Location(x, y)
                if gameMap.getSite(curLoc).owner == myID:
                    movedPiece = False
                    if gameMap.getSite(Location(y, x)).strength == 0:
                        moves.append(Move(curLoc, STILL))
                        analytics['s'] += 1
                        movedPiece = True
                        break
                    if not movedPiece:
                        for d in CARDINALS:
                            f.write(str(gameMap.getSite(curLoc, d).owner) + ' ' + str(gameMap.getSite(curLoc, d).strength) + '\n')
                            if (gameMap.getSite(curLoc, d).owner != myID
                                and gameMap.getSite(curLoc, d).strength
                                < gameMap.getSite(curLoc).strength
                            ):
                                f.write(str(gameMap.getSite(curLoc, d).strength) + ' ' + str(myID) + ' ' + str(d))
                                moves.append(Move(curLoc, d))
                                analytics['m'] += 1
                                movedPiece = True
                                break
                    if not movedPiece:
                        # impossibru
                        moves.append(Move(curLoc, int(random.random() * 5)))
        f.write('kickstarting' + str(analytics) + str(getTerritory(gameMap, myID)) + '\n')
    else:
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
                    if not movedPiece and gameMap.getSite(Location(y, x)).strength == 0:
                        moves.append(Move(curLoc, STILL))
                        analytics['s'] += 1
                        movedPiece = True
                    if not movedPiece:
                        moves.append(Move(curLoc, NORTH if bool(int(random.random() * 2)) else WEST))
                        analytics['m'] += 1
                        movedPiece = True
        f.write(str(analytics) + str(getTerritory(gameMap, myID)) + '\n')
    f.close()
    sendFrame(moves)
    roundCnt += 1
