from pprint import pprint
from re import findall
import pdb

# Problem: Validate sequences according to rules
# Class: recursive?
# 
#
# given page number p
# given all rules ar
#   ret = []
#   for d1,d2 in ar:
#       if d1==p: ret.append((d1,d2))
#   return ret
#
#
# given list of rules lr
# given sequence s
# apply each rule to entire sequence
# for p in sequence
#   rules = get_rules(p)
#   for r in rules:
#       test = s.index(d1) < s.index(d2)
#
#
# given input f
# return list of rules
# ret = []
#   for r in f:
#       d1,d2 = findall(r'(\d)\|(\d)',r)
#       ret.append((d1,d2))
#   return ret
#
# given input f
# return list of page lists
# ret = []
#   for r in f:
#       l = findall(r'(?:(\d),)+',r)
#       ret.append([int(x) for x in l])
#   return ret
#   
# trivial case:
# rules: 1|2
# sequence: 1,2
# 1 -> fetch rules for 1 = (1,2)
# apply rule -> index(1) < index(2) ? -> sequence passes
#
# algorithm:
# for each number in seq:
#   for each rule r_n:
#       if seq digit d_n == r_n[0]:
#           if seq.index(r_n[0]) > seq.index(r_n[1]): return False
# return True
# 
# given sequence s, rules_list r
# for d1,d2 in r:
#   if d1 in s and d2 in s:
#       ret.append(r)

def read_input(inpt):
    rules = []
    pages = []
    with open(inpt,'r') as f:
        while True:
            line = f.readline().strip()
            if line == '': break
            rules.append(line)
        while True:
            line = f.readline().strip()
            if line == '': break
            pages.append(line)
    return rules,pages

def parse_rules(rules):
    ret = []
    for r in rules:
        d1,d2 = findall(r'(\d+)\|(\d+)',r)[0]
        ret.append((int(d1),int(d2)))
    return ret

def parse_pages(pages):
    ret = []
    for p in pages:
        tmp = []
        [tmp.append(int(d)) for d in p.split(sep=',')]
        ret.append(tmp)
    return ret

def fetch_rules(rules, seq):
    ret = []
    for r in rules:
        d1,d2 = r
        if d1 in seq and d2 in seq:
            ret.append(r)
    return ret

rules,pages = read_input('input.txt')

rules = parse_rules(rules)
list_of_books = parse_pages(pages)

test_rule = rules[0]
test_pages = list_of_books[0]

curr_rules =  fetch_rules(rules,test_pages)

def read(book):
    #print(f'Current book: {book}')
    broken_rules = []
    curr_rules = fetch_rules(rules, book)
    #print(f'Current rules: {curr_rules}')
    for rule in curr_rules:
        #print(f'Evaluating rule: {rule}')
        if ck_rule(book,rule):
            broken_rules.append(rule)
            #print(f'Rule violated!')
    return broken_rules

def ck_rule(book,rule):
    b_index = [book.index(r) for r in rule]
    return book.index(rule[0]) > book.index(rule[1])

def read_list_of_books(list_of_books):
    count = 0
    bad_books = []

    for b in list_of_books:
        br = read(b)
        if len(br) > 0: bad_books.append(b)
        else: count+= b[len(b)//2]
    return count,bad_books

def swap(book,rule):
    if not ck_rule(book,rule): return
    d1,d2 = rule
    b1,b2 = book.index(d1), book.index(d2)
    book[b1],book[b2] = book[b2],book[b1]
    return book

def fix_books(bad_books):
    fixed = []
    for book in bad_books:
        curr_rules = fetch_rules(rules, book)
        for rule in curr_rules:
            swap(book,rule)
        fixed.append(book)
    return fixed

def many_fix(bad_books):
    fb = fix_books(bad_books)
    for _ in range(99):
        fb = fix_books(fb)
    return fb

count, bad_books = read_list_of_books(list_of_books)

fb = many_fix(bad_books)

new_count, worse_books = read_list_of_books(fb)

#pprint(vars())
print(new_count)


exit()

#print(fixed)
count = 0
new_books = []
for b in fixed:
    br = read(b)
    if len(br) > 0: 
        print(b)
        new_books.append(b)
    else:
        count+= b[len(b)//2]
print(count)

# Part 2: Fix bad books
# algo: 
#   for each bad_book:
#      for each rule:
#           swap indexes of rule[d1],rule[d2]
