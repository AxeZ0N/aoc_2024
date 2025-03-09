from pprint import pprint

with open('input.txt','r') as f:
    inpt = f.readlines()

def separate_input(inpt):
    inpt = [i.strip() for i in inpt]
    l1,l2 = [],[]
    for i in inpt:
        i1,i2 = i.split()
        l1.append(int(i1))
        l2.append(int(i2))
    return l1,l2

l_list,r_list = separate_input(inpt)
l_list.sort()
r_list.sort()

def get_dist(l_list,r_list):
    for x,y in zip(l_list,r_list):
        yield abs(x-y)

dist_list = [x for x in get_dist(l_list,r_list)]

from itertools import groupby


def count_stuff(l_list):
    return {id:l_list.count(id) for id in l_list}

def do_smth(): pass

def foo():

    rgt_list_dict = count_stuff(r_list)
    total = 0

    for id in l_list:
        times_appear_in_rgt_lst = rgt_list_dict.get(id,0)
        total += id * times_appear_in_rgt_lst
        msg = f'{id} * {times_appear_in_rgt_lst} += {total}'
        print(msg)

    print(total)


foo()
