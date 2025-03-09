from pprint import pprint

card = ('NORTH','EAST','SOUTH','WEST')
c = ('N','E','S','W')
card_inals = ((-1,0),(0,1),(1,0),(0,-1))

CARDINALS = {x:(y,z) for x,y,z in zip(c,card,card_inals)}

print(CARDINALS)

class Plot:
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color
        self.walls = (c for _ in range(4))


class Blob:
    garden = [[None],]
    def is_border(self, coords, direction):
        i,j = coords
        di,dj = CARDINALS[direction][1]
        return self.garden[i][j].color == self.garden[i+di][j+dj].color


with open('input.txt','r') as f:
    garden = []
    for i,row in enumerate(f):
        tmp = []
        for j,c in enumerate(row):
            tmp.append(Plot((i,j),c))
        garden.append(tmp)
    sl = len(garden)

class Garden:
    garden = [[None],]
    def __init__(self, garden):
        self.garden = garden


G = Garden(garden)

P = Plot((0,0),None)
B = Blob()

print(P.color)

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

