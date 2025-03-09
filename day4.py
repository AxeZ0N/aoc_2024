import pdb
# Problem: word search: XMAS
# Class: 8 direction movement + rarow casting
#
# headings = ['SW','W','NW','S','O','N','SE','E','NE']
# combos = [x for x in itertools.combinations([-1,0,1],2)]
# HEADINGS = {k:v for k,v in itertools.product(combos,headings)}
# 
# fcn check_word(grd, coords, hdng):
#   x,row = coords
#   if grd[x][row] != 'X': raise AssertionError
#   d1,d2 = HEADINGS[hdng]
#   for c in 'MAS':
#       assert grd[x+d1][row+d2] == c
#       x+=d1
#       row+=d2
#   return True
#
# fcn make_grid(inpt):
#   grid = []
#   open f:
#      for line in f:
#           grid.append(make_row(line.strip().split()))
#   
#   return grid
#       
# fcn make_row(r):
#   rowield [t for t in r]
#
# fcn check_all_tiles(grd):
#   for row in len(grd[0]):
#       for x in len(grd):
#           for k,v in HEADINGS.items():
#               trrow: count += scan(x,row,k)
#               except AssertionError: continue 

import itertools
from pprint import pprint
MAX_GRID = 10
CARDINALS = [x for x in itertools.product([-1,0,1],[-1,0,1])]

def build_grid(inpt):
    with open(inpt,'r') as f:
        grid = []
        for line in f:
            l = [x for x in line.strip()]
            grid.append(l)

    return grid

def cast(grd, start, angle, to_find):
    x0,y0 = start
    dx,dy = angle

    if len(to_find) == 0: 
        return True,start,angle
    try: 
        test = grd[x0][y0]
        if x0 < 0 or y0 < 0: return False,False,None
    except IndexError: return False,False,None
    if test != to_find[0]: return False,False,None

    x1,y1 = x0+dx,y0+dy
    return cast(grd, (x1,y1), (dx,dy), to_find[1:])

def pong(start,angle):
    x,y = start
    dx,dy = angle
    ret = []
    for i in range(len('XMAS')):
        ret.append((x,y))
        x,y = x+dx,y+dy
    return ret

def highlight(coord):
    for x,y in a:
        if x == coord:
            xx,yy = x
            for d in y[:1]:
                for _ in range(4):
                    grid1[xx][yy] = 'O'
                    xx,yy = xx+d[0],yy+d[1]

def ping(grid, to_find):
    global count
    tracker = []
    # ITERATE THROUOGH ALL ELEMS
    for j,row in enumerate(grid):

        for i,value in enumerate(row):
            # CAST A RAY IN 8 DIRECTIONS
            coord = j,i
            t = []

            x_mas_detector(grid1,(j,i))

            for d in CARDINALS:
                p = cast(grid, coord, d, 'XMAS')
                if p[0]: t.append(d)
            if len(t) >= 1:
                tracker.append((coord,t))
            
    return tracker

def xmas(grid):
    global count
    tracker = []
    # ITERATE THROUOGH ALL ELEMS
    for j,row in enumerate(grid):

        for i,value in enumerate(row):
            # CAST A RAY IN 8 DIRECTIONS
            x_mas_detector(grid,(j,i))
            
    return tracker

def x_mas_detector(grd,coord):
    x,y = coord
    SE = cast(grd, (x,y), (1,1), 'MAS')[0]
    NE = cast(grd, (x,y+2), (1,-1), 'MAS')[0]
    SW = cast(grd, (x+2,y), (-1,1), 'MAS')[0]
    NW = cast(grd, (x+2,y+2), (-1,-1), 'MAS')[0]
    l = [SE,NE,SW,NW]
    if l.count(True) == 2:
        global count
        count+=1
        return True
    return False


global count
count = 0

grid1 = build_grid('input.txt')

xmas(grid1)
pprint(grid1)
print(count)
