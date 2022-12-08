from aocd import lines

class ElfFile:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

ELF = ElfFile('/')
pwd = ELF 

for line in lines:
    if line.startswith('$'):
        p = line.split()
        cmd = p[1]
        if cmd == 'cd':
            dir = p[2]
            if dir == '..':
                pwd = pwd.parent
            else:
                f = ElfFile(dir)
                f.parent = pwd
                pwd.children.append(f)
                pwd = f
    else:
        size, name = line.split()
        if size != 'dir':
            f = ElfFile(name, int(size))
            pwd.children.append(f)

SIZES = {}

def dir_size(f):
    if not f.children:
        return f.size
    total_size = 0
    for c in f.children:
        total_size += dir_size(c)

    SIZES[f] = total_size
    return total_size

USED = dir_size(ELF)

print("Part 1:", sum(s for s in SIZES.values() if s < 100000))

TOTAL = 70000000
NEED = 30000000
FREE = TOTAL - USED

for size in sorted(SIZES.values()):
    if FREE + size >= NEED:
        print("Part 2:",size)
        break

