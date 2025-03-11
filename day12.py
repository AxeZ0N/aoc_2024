# problem class: graph theory
# algo: test spreading color blocks, nodes are 'plots'
#
# description:
#   recursively check each cardinal, for each coord
#   track whether i,j -> i+di,j+dj is blob border
#
# base case:
#   return tile == blob
#
# loops:
#   for each i,j in coords:
#    if i,j not in blob:
#     for each cardinal direction:
#       if base case: blob.add(i,j)
#
# test whether given line seg is border
#   if plot[i][j].color == plot[x][y].color
#
# test each cardinal for border status
#   curr_plot = i,j
#   for C in CARDINALS:
#       x,y = C
#       self.walls[C] = self.test_border(C: <CARDINAL>)
#
# if plot has all 4 walls, it's an orphan
# if plot has < 4 walls, it's part of a blob
# map borders act as walls
# # # # 
#
# base case for sim
#   Plot: ( (x,y), Color )
#   Garden = [ Plot, ]
#   Perimeter: (Plot1,Plot2) where x2,y2 = x1+-1,y1+-1 and Color1 != Color2
#   Area: [ Plot.color1, Plot.color1, ... ] 

from pprint import pprint
from collections import defaultdict, Counter
from dataclasses import dataclass


@dataclass
class Plot:
    coords: int
    color: str

    def __add__(self, x): return self.coords[0]+x.coords[0], self.coords[1]+x.coords[1]
    def __sub__(self, x): return self.coords[0]+-x.coords[0], self.coords[1]+-x.coords[1]
    def __abs__(self): return abs(self.coords[0]), abs(self.coords[1])

def get_input():
    with open('input.txt','r') as f:
        for i,line in enumerate(f.readlines()):
            for j,plot in enumerate(line.strip()):
                yield (i,j,plot)

def are_touching(plot1,plot2):
    print(plot1,plot2)
    (x1,y1),(x2,y2) = plot1.coords, plot2.coords
    dx,dy = abs(x2-x1),abs(y2-y1)
    return dx,dy == 0,1 or dx,dy == 1,0

def is_perimeter(plot1,plot2):
    if are_touching(plot1,plot2) and plot1.color != plot2.color: return True
    else: return False

GARDEN = [Plot((i,j),x) for i,j,x in get_input()]

PERIMETERS = defaultdict(set,)



print(list(get_input()))

print(GARDEN)

AREAS = Counter([x.color for x in GARDEN])

print(AREAS)
