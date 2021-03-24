from display import *
from matrix import *

def add_point(m, p):
    for i in range(3):
        m[i].append(p[i])
    m[3].append(1)

def add_edge(m, p1, p2):
    add_point(m, p1)
    add_point(m, p2)

def draw_line(x0, y0, x1, y1, screen, color):
    if abs(x1 - x0) > abs(y1 - y0):
        if x1 > x0:
            draw_linex(x0, y0, x1, y1, screen, color)
        else:
            draw_linex(x1, y1, x0, y0, screen, color)
    else:
        if y1 > y0:
            draw_liney(x0, y0, x1, y1, screen, color)
        else:
            draw_liney(x1, y1, x0, y0, screen, color)

def draw_linex(x0, y0, x1, y1, screen, color):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    A = abs(y1 - y0)
    a = y1 - y0
    k = 1 if A == a else -1
    B = x1 - x0
    Z = 2 * B - A
    y = y0
    for x in range(x0, x1):
        plot(screen, color, x, y)
        if Z > 0:
            y += k
            Z -= 2 * B
        Z += 2 * A

def draw_liney(x0, y0, x1, y1, screen, color):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    B = y1 - y0
    A = abs(x1 - x0)
    a = x1 - x0
    k = 1 if A == a else -1
    Z = 2 * B - A
    x = x0
    for y in range(y0, y1):
        plot(screen, color, x, y)
        if Z > 0:
            x += k
            Z -= 2 * B
        Z += 2 * A

def draw_2D_edges(m, screen, color):
    for i in range(0, len(m[0]), 2):
        draw_line(m[0][i], m[1][i], m[0][i+1], m[1][i+1], screen, color)
