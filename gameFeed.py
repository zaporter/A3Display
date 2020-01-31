import time
from basicDisp import *


def game_clear(input_file):
    fp = open(input_file, 'w')
    fp.close();


def game_popCommand(input_file):
    rp = open(input_file, 'r')
    lines = rp.readlines()
    rp.close()
    fp = open(input_file,'w+')
    if (len(lines)==0):
        return ""
    for x in range(len(lines)-1):
        fp.write(lines[x+1])
    fp.close()
    return lines[0].rstrip("\n\r")


