import time
from basicDisp import *


def game_clear():
    fp = open(GAME_FILE, 'w')
    fp.close();

def game_pullCommands():
    fp = open(GAME_FILE, 'r')
    lines = []
    line = fp.readline()
    while (line):
        lines.append(line)
        line=pf.readline()
    fp.close()



