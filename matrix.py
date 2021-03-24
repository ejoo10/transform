import math

def matrix_multiply(m1, m2):
    m = []
    for i in range(len(m1)):
        r = []
        try:
            for j in range(len(m2[0])):
                s = 0
                for x in range(len(m1[i])):
                    s += m1[i][x] * m2[x][j]
                r.append(s)
            m.append(r)
        except TypeError:
            s = 0
            for x in range(len(m1[i])):
                s += m1[i][x] * m2[x]
            m.append(s)
    return m

def identity(n):
    m = []
    for i in range(n):
        r = []
        for j in range(n):
            if (i == j):
                r.append(1)
            else:
                r.append(0)
        m.append(r)
    return m

def matrix_print(m):
    for i in range(len(m)):
        for j in m[i]:
            print(str(j)),
        print("\n"),

def translate(x, y, z):
    return [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]

def scale(x, y, z):
    return [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]

def rotatex(theta):
    t = math.pi * theta / 180
    return [[1, 0, 0, 0], [0, math.cos(t), -math.sin(t), 0], [0, math.sin(t), math.cos(t), 0], [0, 0, 0, 1]]

def rotatey(theta):
    t = math.pi * theta / 180
    return [[math.cos(t), 0, math.sin(t), 0], [0, 1, 0, 0], [-math.sin(t), 0, math.cos(t), 0], [0, 0, 0, 1]]

def rotatez(theta):
    t = math.pi * theta / 180
    return [[math.cos(t), -math.sin(t), 0, 0], [math.sin(t), math.cos(t), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
