#!/usr/bin/python3
from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit('zyzo')
f = open('logfile.log', 'w')
f.write('')
f.close()
while True:
    moves = []
    gameMap = getFrame()
    f = open('logfile.log', 'a')
    analytics = { 's': 0, 'a': 0, 'm': 0 }
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            if gameMap.getSite(Location(x, y)).owner == myID:
                movedPiece = False
                for d in CARDINALS:
                    if (
                        gameMap.getSite(Location(x, y), d).owner != myID
                        and gameMap.getSite(Location(x, y), d).strength
                        < gameMap.getSite(Location(x, y)).strength
                    ):
                        moves.append(Move(Location(x, y), d))
                        analytics['a'] += 1
                        movedPiece = True
                        break
                if not movedPiece and gameMap.getSite(Location(y, x)).strength == 0:
                    moves.append(Move(Location(x, y), STILL))
                    analytics['s'] += 1
                    movedPiece = True
                if not movedPiece:
                    moves.append(Move(Location(x, y), int(random.random() * 5)))
                    analytics['m'] += 1
                    movedPiece = True
    f.write(str(analytics['s']) + 's ' + str(analytics['m']) + 'm ' + str(analytics['a']) + 'a\n')
    f.close()
    sendFrame(moves)
