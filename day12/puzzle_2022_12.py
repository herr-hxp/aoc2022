from aocd import data
from aocd import lines
from collections import deque

row = len(lines)
char = len(lines[0])
alt = [[0 for _ in range(char)] for _ in range(row)]

for r in range(row):
    for c in range(char):
        if lines[r][c] == 'S':
            #print(r,c)
            #print('We got S')
            alt[r][c] = 1
        elif lines[r][c] == 'E':
            #print('We got E')
            #print(r,c)
            alt[r][c] = 26
        else:
            alt[r][c] = ord(lines[r][c])-ord('a')+1

def climb(pt):
    board = deque()
    for r in range(row):
        for c in range(char):
            if (pt==1 and lines[r][c] == 'S') or (pt==2 and alt[r][c] == 1):
                board.append(((r,c),0))
    myset = set()
    while board:
        (r,c,),d = board.popleft()
        if (r,c) in myset:
            continue
        myset.add((r,c))
        if lines[r][c] == 'E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0 <= rr < row and 0 <= cc < char and alt[rr][cc] <= 1 + alt[r][c]:
                board.append(((rr,cc),d+1))

print(climb(1))
print(climb(2))
