# input is wicked long line of digits.
# digits alternate between representing file_sizes, and representing free_spaces (in Blocks)
# files are numbered based on inital order starting from 0
# submission is checksum, "add up the result of multiplying each of these blocks' position with the file ID number it contains"
# can't tell what the twist is yet. Might be crazy big ints. Might just be complicated

# task: left zip reversed? Compress and Uncompress. move each file block to leftmost free space, calculate checksum
# Going to attempt to make the test inputs match so I can get a better idea of the solution space
# I think the twist is that you can't simulate the entire uncompressed file system, so you need to do operations on the disk map
# Maybe. It does seem like the most obvious way to compress the data is as stated in the example.


class Free:
    def __init__(self,size):
        self.size=size

class File: 
    def __init__(self,size,id):
        self.size = size
        self.id = id

with open('input.txt','r') as f:
    inpt = f.readlines()

disk_map = inpt.pop(0).strip()

curr_id = 0
filesystem = []

# algo to unzip disk_map:
# for each digit in disk_map:
#   if state is file:
#       cur_f = File(digit,curr_id)
#       curr_id+=1
#
#   if state is free:
#       cur_f = Free(digit)
#
#   filesystem.append(cur_f)
#   toggle state bit

# algo to re-zip disk_map:
# for f in filesystem:
#   if f is File:
#       disk_map = f'{disk_map}{f.size}'
#
#   if f is Free:
#       disk_map = f'{disk_map}{f.size}'

# algo to compress data:
# it's the same as re-merging in mergesort.
# while disk_map[ptr1] != free: ptr1+=1
# while disk_map[ptr2] != file: ptr1+=1


for i,digit in enumerate(disk_map):
    if i % 2 == 0: state='file'
    else: state='free'
    digit = int(digit)

    if state=='file': filesystem.append(File(digit,curr_id))
    elif state=='free': filesystem.append(Free(digit))

print(filesystem)
print(len(filesystem))
