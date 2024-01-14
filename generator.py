import random

LENGTH = 7
LIST_NAME = "lst"
OUTPUT_NAME = "sorted"

buffer = ""
nums = set(range(LENGTH))


def line(n, t, f):
    condition = "if" if f else "elif"
    comparisons = " and ".join([f"{LIST_NAME}[{n}] <= {LIST_NAME}[{i}]" for i in nums])
    line = '\t' * t + f"{condition} {comparisons}:\n"
    assignment = '\t' * (t + 1) + f"{OUTPUT_NAME}[{t}] = {LIST_NAME}[{n}]\n"
    
    res = line + assignment
    if len(nums) == 1:
        res += '\t' * (t + 1) + f"{OUTPUT_NAME}[{t + 1}] = {LIST_NAME}[{list(nums)[0]}]\n"
    
    return res + '\n'
    

def generate_code():
    global buffer
    buffer += f"{LIST_NAME} = {random.sample(range(-10000, 10001), LENGTH)} # enter your array here\n"
    buffer += f"assert len({LIST_NAME}) <= {LENGTH}, 'array length must be between 0 and {LENGTH}.'\n"
    buffer += f"if len({LIST_NAME}) < {LENGTH}:\n"
    buffer += "\t" + f"{LIST_NAME}.extend([0] * ({LENGTH} - len({LIST_NAME})))\n"
    buffer += f"{OUTPUT_NAME} = [0] * {LENGTH}\n\n"
    construct(0, True)
    buffer += f"print({OUTPUT_NAME})\n"


def construct(t, f):
    global buffer
    for i in nums.copy():
        nums.remove(i)
        if len(nums) > 0:
            buffer += line(i, t, f)
        f = False
        construct(t + 1, True)
        nums.add(i)

generate_code()

with open('my_first_sort.py', 'w') as file:
    file.write(buffer)
