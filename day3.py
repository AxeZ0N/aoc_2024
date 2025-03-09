from re import findall

inpt=[]

with open('input.txt', 'r') as f:
    for line in f:
        inpt.append(line)

my_list = []
for line in inpt:
    my_list.append(findall(r"do\(\)|don\'t\(\)|mul\(\d+\,\d+\)",line))

global enable
enable = True

def case_do():
    global enable
    enable = True

def case_dont():
    global enable
    enable = False

def case_mul(mul_str):
    d1,d2 = findall(r"(\d+)\,(\d+)", mul_str)[0]
    return int(d1) * int(d2)

def flatten(l):
    p = []
    [[p.append(x) for x in y] for y in l]
    return p


my_list = flatten(my_list)
i = 0
total=0

while i < len(my_list):
    cur_instr = my_list[i]
    match cur_instr:
        case 'do()': case_do()
        case 'don\'t()': case_dont()

    if 'mul' in cur_instr:
        ret = case_mul(cur_instr)
        if enable:
            total+=ret
    i+=1
print(total)
