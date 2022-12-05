import fileinput
import re

data = ''.join(fileinput.input(files=('input')))
crates, moves = data.split('\n\n')

crates = list(
    "".join(x).strip()[1:]
        for i, x in enumerate(
            zip(*map(list, crates.split("\n")[::-1]))
        )
        if i % 4 == 1
)
moves = [
    tuple(map(int, re.findall(r"\d+", move)))
        for move in moves.strip().split("\n")
]
    
def crane(pt2 = False):
    _crates = [ None ] + crates[:]
    for N, a, b in moves:
        _crates[a], m = _crates[a][:-N], _crates[a][-N:]
        if not pt2:
            m = m[::-1]
        _crates[b] = _crates[b] + m
        
    return "".join(stack[-1] for stack in _crates[1:])
    
print("Part 1:", crane())
print("Part 2:", crane(True))
