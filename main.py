from matrix import *
from draw import *
from display import *
from parse import *
import math
import random

s = new_screen()
c = [ 255, 0, 0 ]

edges = [[], [], [], []]
m = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
parse("script", edges, m, s, c)
