# problem class: graph theory
# base case for sim
#   All non-contiguous symbols are unique
#   Plot: ( (x,y), Color )
#   Blob: Plot of Color C and tiles touching
#   Garden = [ Plot, ]
#   Perimeter: (Plot1,Plot2) where x2,y2 = x1+-1,y1+-1 and Color1 != Color2
#   Area: [ Plot.color1, Plot.color1, ... ] 

from pprint import pprint
from collections import defaultdict, Counter
from dataclasses import dataclass
from itertools import product, pairwise


@dataclass
class Plot:
    coords: int
    color: str
    blob: int = None

def get_input():
    seen = set()
    with open('input.txt','r') as f:
        for i,line in enumerate(f.readlines()):
            for j,plot in enumerate(line.strip()):
                yield (i,j,plot)

def are_touching(plot1,plot2):
    (x1,y1),(x2,y2) = plot1.coords, plot2.coords
    dx,dy = abs(x2-x1),abs(y2-y1)
    match (dx,dy):
        case (0,1): return True
        case (1,0): return True
        case _: return False

def is_perimeter(plot1,plot2):
    if are_touching(plot1,plot2) and plot1.color != plot2.color: return True
    else: return False

GARDEN = [Plot((i,j),x) for i,j,x in get_input()]

BLOB_COUNTER = 0
for g in GARDEN:
    if g.blob is None: 
        touch_plot = [p for p in GARDEN if are_touching(p,g)]
        for tp in touch_plot:
            if tp.blob is not None and tp.color == g.color: 
                g.blob = tp.blob
        if g.blob is None:
            g.blob = BLOB_COUNTER
            BLOB_COUNTER+=1

AREAS = defaultdict(int)

for curr_blob in range(BLOB_COUNTER):
    for g in GARDEN:
        if g.blob == curr_blob: AREAS[g.blob] += 1

PERIMS = defaultdict(int)


count = 0

for g in GARDEN:
    touch_plot = [p for p in GARDEN if are_touching(p,g)]
    for tp in touch_plot:
        if tp.color == g.color: continue
        PERIMS[g.blob]+=1


print(count)
print(PERIMS)
