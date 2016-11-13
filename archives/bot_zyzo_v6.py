"""
Naive bot
"""
#!/usr/bin/python3
from hlt import (
    Location, Move,
    CARDINALS, STILL
)
from networking import (
    getInit, sendInit, getFrame, sendFrame
)
from helper import (
    getStrength, getTerritory, getProduction
)



sendInit('zyzo')
FILE_WRITER = open('log-ANALYTICS.log', 'w')
FILE_WRITER.write('')
FILE_WRITER.close()

MY_ID, GAME_MAP = getInit()
while True:
    MOVES = []
    GAME_MAP = getFrame()
    FILE_WRITER = open('log-analytics.log', 'a')
    ANALYTICS = {'s': 0, 'a': 0, 'm': 0}
    for y in range(GAME_MAP.height):
        for x in range(GAME_MAP.width):
            curLoc = Location(x, y)
            if GAME_MAP.getSite(curLoc).owner == MY_ID:
                movedPiece = False
                for d in CARDINALS:
                    if (
                            GAME_MAP.getSite(curLoc, d).owner != MY_ID
                            and GAME_MAP.getSite(curLoc, d).strength
                            < GAME_MAP.getSite(curLoc).strength
                    ):
                        MOVES.append(Move(curLoc, d))
                        ANALYTICS['a'] += 1
                        movedPiece = True
                        break
                if not movedPiece:
                    MOVES.append(Move(curLoc, STILL))
                    ANALYTICS['s'] += 1
                    movedPiece = True
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
