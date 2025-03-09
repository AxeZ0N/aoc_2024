import dataclasses
import itertools
from pprint import pprint
import pdb

def read_report(fname):
    reports_list = []
    with open(fname,'r') as f:
        for line in f:
            reports_list.append(Report([int(x) for x in line.split()]))

    return reports_list


class Report:
    levels = []
    def __init__(self,levels):
        self.levels = levels
        self.is_increasing = self.levels[0] < self.levels[1]
    def __repr__(self):
        return str(self.levels)

def _ck(levels):
    l = list(itertools.pairwise(levels))
    pprint(levels)
    a = list(map(lambda x: x[0] < x[1], l))
    is_incr = all(a)

    b = list(map(lambda x: x[0] > x[1], l))
    is_decr = all(b)

    c = list(map(lambda x: abs(x[0]-x[1]) <= 3, l))
    is_smooth = all(c)

    foo = (all(a) != all(b)) & all(c)
    return foo

all_reports = read_report('input.txt')

pw = lambda l: [l for l in itertools.pairwise(l)]

shipt = []
with open('input.txt','r') as f:
  for line in f:
    a = line.strip().split()
    a = [int(x) for x in a]
    shipt.append(a)


global count
count = 0

def loops(levels):
  for i in range(len(levels)):
    c = levels.copy()
    c.pop(i)
    print(f'current perm {c}')
    ret = classify(c, True)
    if ret is None: 
      print(f'perm {c} success!')
      return None
  return False


def test_incr(levels):
  print(f'Testing incr: {levels}')
  i = 0
  while i < len(levels) - 1:
    x1,x2 = levels[i],levels[i+1]
    if x1 > x2: return False
    elif x1 == x2: return False
    elif abs(x1-x2) > 3: return False
    else: i += 1

def test_equal(levels):
  return False

def test_decr(levels):
  print(f'Testing decr: {levels}')
  i = 0
  while i < len(levels) - 1:
    x1,x2 = levels[i],levels[i+1]
    if x1 < x2: return False
    elif x1 == x2: return False
    elif abs(x1-x2) > 3: return False
    else: i += 1


def classify(levels, flag=False):
  print(f'Classifying: {levels}')
  x1,x2 = levels[0],levels[1]

  if x1 > x2:
    incr = False
    decr = True
    equal = False
  elif x1 < x2:
    incr = True
    decr = False
    equal = False
  elif x1 == x2:
    incr = False
    decr = False
    equal = True

  if incr: ret = test_incr(levels)
  elif decr: ret = test_decr(levels)
  elif equal: ret = test_equal(levels)

  if ret is False and not flag: 
    print(f'Permuting {levels}')
    twach = loops(levels)
  elif ret is None: 
    global count
    count += 1
    return None
  return False


print(shipt)
count = 0
for lev in shipt:
  a = classify(lev)
print(count)

