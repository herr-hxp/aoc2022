from aocd import data
from aocd import submit

pt1 = None
pt2 = None

def scanner(part,num):
    for i in range(len(data)):
        seq = data[i:i+num]
        if len(seq) == len(set(seq)) and not part:
            print(set(seq))
            part = i + num
    return part

pt1 = scanner(pt1,4)
pt2 = scanner(pt2,14)

print("Part 1:", pt1)
print("Part 2:", pt2)

submit(pt1, part="a")
submit(pt2, part="b")
