from pprint import pprint
from itertools import permutations, zip_longest, product
from re import findall
import copy
import pdb

with open('input.txt','r') as f:
    lines = [x.strip() for x in f]

result = []
nums = []
ops = ['+','*','||']

d = {'*':lambda x,y: x*y,'+':lambda x,y: x+y}
d2 = {'*':lambda x,y: x*y,'+':lambda x,y: x+y,'||':lambda x,y: int(str(x)+str(y))}

class InvalidComboException(Exception): pass


def get_ints(equa):
    a = findall(r'(\d+)',equa)
    result.append(int(a[0]))
    nums.append([int(x) for x in a[1:]])
    return result[-1],a[1:]

def build_ml(to_parse, ops):
    mathlist = []
    n_ops = len(to_parse) - 1
    ops_perms = list(product(ops,repeat=n_ops))
    for perms in ops_perms:
        n2 = copy.deepcopy(to_parse)
        ml = []
        for x in perms:
            ml.append(n2.pop(0))
            ml.append(x)
        ml.append(n2.pop(0))
        mathlist.append(ml)
        ml=[]
    return mathlist

def reduce(l,r=None):
    while len(l) > 1:
        n1,op,n2 = [l.pop(0) for _ in range(3)]
        ret = d2[op](n1,n2)
        l.insert(0,ret)
        if r is not None:
            if l[0] > r: raise InvalidComboException
    return l.pop(0)


def do_math(nums,r):
    for nlist in nums:
        try: 
            ret = reduce(nlist)
            if ret == r: return True
        except InvalidComboException: return False
    return False


dd = [get_ints(x) for x in lines]

def larry(nums,ops):
    count = 0
    for nlist,r in zip(nums,result):
        mathlist = build_ml(nlist, ops)
        a = do_math(mathlist,r)
        if a: count+=r
        if count % 10 >= 0:
            print(count)
    return count


print(larry(nums,ops))
