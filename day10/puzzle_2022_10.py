from aocd import lines

# part 1 
X = 1
cycle = 0
vip_cycles = [20,60,100,140,180,220]
signal_strength = 0

# part 2 CRT properties
WIDTH = 40

# draw on the CRT screen
def draw():
    position = ((cycle - 1) % WIDTH) + 1
    if X <= position < X + 3:
        # we dont want print to end with a newline and so we modify it with the end parameter
        print("#", end="")
    else:
        print(".", end="")
    if position == WIDTH: # if we've reached the end of the width, print a newline
        print()

for line in lines:
    instruction = line.split()
    operation = instruction[0]

    if operation == 'noop':
        cycle += 1
        draw()
        if cycle in vip_cycles:
            signal_strength += X * cycle
    
    elif operation == 'addx':
        argument = int(instruction[1])
        # first cycle
        cycle += 1
        draw()
        if cycle in vip_cycles:
            signal_strength += X * cycle
        # second cycle
        cycle += 1
        draw()
        if cycle in vip_cycles:
            signal_strength += X * cycle
        X += int(argument)

print("Part 1:", signal_strength)


