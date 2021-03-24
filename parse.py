from display import *
from matrix import *
from draw import *

def parse(name, edges, m, s, c):
    f = open(name)
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i] == "line\n":
            k = lines[i+1].split()
            add_edge(edges, [int(k[0]), int(k[1]), int(k[2])], [int(k[3]), int(k[4]), int(k[5])])
            i += 1
        elif lines[i] == "ident\n":
            m = identity(4)
        elif lines[i] == "scale\n":
            k = lines[i+1].split(" ")
            m = matrix_multiply(scale(float(k[0]), float(k[1]), float(k[2])), m)
            i += 1
        elif lines[i] == "move\n":
            k = lines[i+1].split(" ")
            m = matrix_multiply(translate(int(k[0]), int(k[1]), int(k[2])), m)
            i += 1
        elif lines[i] == "rotate\n":
            k = lines[i+1].split(" ")
            if k[0] == "x":
                m = matrix_multiply(rotatex(float(k[1])), m)
            elif k[0] == "y":
                m = matrix_multiply(rotatey(float(k[1])), m)
            elif k[0] == "z":
                m = matrix_multiply(rotatez(float(k[1])), m)
            i += 1
        elif lines[i] == "apply\n":
            edges = matrix_multiply(m, edges)
        elif lines[i] == "display\n":
            clear_screen(s)
            draw_2D_edges(edges, s, c)
            display(s)
        elif lines[i] == "save\n":
            clear_screen(s)
            draw_2D_edges(edges, s, c)
            save_ppm_ascii(s, lines[i+1])
        i += 1
