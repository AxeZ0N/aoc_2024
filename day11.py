import itertools
import collections
from time import time
from pprint import pprint

with open('input.txt','r') as f:
    inpt = f.readline().strip().split()

def r1(stone): return '1'
def r2(stone): return [str(int(x)) for x in (stone[:len(stone)//2],stone[len(stone)//2:])]
def r3(stone): return [str(int(stone)*2024)]

def cycle(inpt,nuge):
    is_even = lambda x: not len(x) % 2

    stones_ = []
    num = None
    num1 = None
    num2 = None

    for x in inpt:

        if not int(x):
            num = r1(x)
            if num not in nuge: nuge[num]=0
            stones_.append(r1(x))

        elif is_even(x):
            num1,num2 = r2(x)
            if num1 not in nuge: nuge[num1]=0
            if num2 not in nuge: nuge[num2]=0
            stones_.extend(r2(x))

        else:
            num = r3(x)
            if num not in nuge: nuge[num]=0
            stones_.append(r3(x))

        if num is not None: nuge[num] += 1
        if num1 is not None: nuge[num1] += 1
        if num2 is not None: nuge[num2] += 1
        nuge[x] -= 1
        
    return stones_, nuge

stones_dict = collections.defaultdict(lambda: 0)

curr_line = inpt
is_even = lambda x: not len(x) % 2

def blink():
    stones_to_add = []
    for stone in curr_line:
        stones_dict[stone]-=1
        if not int(stone): new_stone = r1(stone)
        elif is_even(stone): new_stone = r2(stone)
        else: new_stone = r3(stone)

        for s in new_stone: stones_dict[s]+=1
    return stones_to_add

#blink()

from collections import defaultdict, OrderedDict

place_holder_stones = defaultdict(lambda: 0,)

line_of_stones = []

lineup = inpt
for stone in lineup:
    place_holder_stones[stone] += 1

for _ in range(76):
    p = 0
    new_line = []
    curr_line = defaultdict(lambda: 0,)

    for stone,count in place_holder_stones.items():
        temp_stone = None
        p+=count

        if stone == '0':
            temp_stone = r1(stone)
            curr_line[temp_stone]+= count
            continue

        elif is_even(stone):
            ts1, ts2 = r2(stone)
            curr_line[ts1]+=count
            curr_line[ts2]+=count
            continue

        elif not is_even(stone):
            temp_stone  = r3(stone)[0]
            curr_line[temp_stone]+=count
            continue

        raise Exception

    place_holder_stones = curr_line
    #print(place_holder_stones.keys())
    #print(place_holder_stones.values())

c = 0
total = sum(place_holder_stones.values())
print(p)
#print(total)
