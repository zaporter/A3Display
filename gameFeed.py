import time
from basicDisp import *


def game_clear():
    fp = open(GAME_FILE, 'w')
    fp.close();


def game_popCommand():
    rp = open(GAME_FILE, 'r')
    lines = rp.readlines()
    rp.close()
    fp = open(GAME_FILE,'w+')
    if (len(lines)==0):
        return ""
    for x in range(len(lines)-1):
        fp.write(lines[x])
    fp.close()
    return lines[len(lines)-1].rstrip("\n\r")


