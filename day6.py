import timeit
from pprint import pprint
from time import time
tic = time()


arrows = {'^':'>','>':'v','v':'<','<':'^'}
headings = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}


lines = []
barriers = set()


with open('input.txt','r') as f:
    for i,row in enumerate(f):
        row = row.strip()
        tmp = []
        for j,c in enumerate(row.strip()):
            if c == '#': barriers.add((i,j))
            if c in arrows: guard_info = ((i,j), c)
        [tmp.append(c) for c in row]
        lines.append(tmp)
    sl = len(lines)

guard_start_pos = guard_info

def is_in_bounds(c1):
    for c in c1:
        if c >= sl or c < 0: return False
    return True


def add(c1, c2):
    return (c1[0]+c2[0],c1[1]+c2[1])


class Map:
    trace = set()
    def step(guard_info,barriers):
        guard_pos, guard_hdg = guard_info
        new_pos = add(guard_pos, headings[guard_hdg])

        for _ in range(4):
            if not new_pos in barriers: break
            guard_hdg = arrows[guard_hdg]
            new_pos = add(guard_pos, headings[guard_hdg])

        guard_info = new_pos,guard_hdg
        if not is_in_bounds(new_pos): return guard_pos,'$'
        if guard_info in Map.trace:
            return guard_pos,'&'
        else:
            Map.trace.add(guard_info)

        return guard_info


def is_loop(guard_info, barrier_pos):
    barriers.add(barrier_pos)
    Map.trace = set(guard_info)
    trace_len = 0
    while True:
        guard_info = Map.step(guard_info,barriers)

        if guard_info[1] == '$':
            barriers.remove(barrier_pos)
            return False

        if guard_info[1] == '&':
            barriers.remove(barrier_pos)
            return True

def run_sim(guard_info):
    Map.trace = set(guard_info)
    while True:
        guard_info = Map.step(guard_info,barriers)
        if guard_info[1] == '$': break

    path = []
    #[path.append(x) for x,y in Map.trace if x not in path]
    [path.append(t[0]) for t in Map.trace if t[0] not in path]
    return  path


guard_info = guard_start_pos
path = run_sim(guard_info)
print(len(path))
guard_info = guard_start_pos
loops = []
for p in path:
    guard_info = guard_start_pos
    a = is_loop(guard_info, p)
    if a: loops.append(p)
    print((path.index(p) / len(path))* 100)
print(len(loops))
toc = time()
print(toc-tic)
