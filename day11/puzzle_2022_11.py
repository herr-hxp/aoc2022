from aocd import data
from copy import deepcopy
from collections import Counter, deque

def anticipate(monkeys, turns, pt2=False):
    monkeys = deepcopy(monkeys)
    mod = 1
    for m in monkey_list:
        mod = (mod*m[2])
    counter = Counter()

    for turn in range(turns):
        for i, (items,op,div,true,false) in enumerate(monkeys):
            for _ in range(len(items)):
                counter[i] += 1
                item = monkeys[i][0].popleft()
                oper, val = op.split()[-2:]
                if val == 'old':
                    val = item
                else:
                    val = int(val)
 
                if oper == "*":
                    item *= val
                elif oper == "+":
                    item += val
                
                if pt2:
                    item %= mod
                else:
                    item //= 3

                next_monkey = true if item % div == 0 else false
                monkeys[next_monkey][0].append(item)
    ins = list(sorted(counter.values(), reverse=True))
    return ins[0] * ins[1]


# init monkey list
monkey_list = []

# get the needed value of each monkey and remove the text
for monkey in data.split('\n\n'):
    m, start_items, op, div, true, false = monkey.split('\n')
    items = deque([int(i) for i in start_items.split(':')[1].split(',')])
    op = op.split(': ')[1]
    div = int(div.split()[-1])
    true = int(true.split()[-1])
    false = int(false.split()[-1])
    monkey_list.append([items,op,div,true,false])
    #print(m)
    #print(items)
    #print(op)
    #print(div)
    #print(true)
    #print(false)

print("Part 1:", anticipate(monkey_list, 20))
print("Part 2:", anticipate(monkey_list, 10000, pt2=True))
#print(monkey_list)
