def countprio(k):
    if k >= "a":
        return ord(k) - ord('a') + 1
    else:
        return ord(k) - ord('A') + 27

# part 1
pt1prio = 0
with open ('input', 'r') as file:
    data = [x.rstrip() for x in file]
    for line in data:
        # split the string in half to two new strings
        x = len(line) // 2
        left = line[:x]
        right = line[x:]
        # put each character of the strings in a set
        sleft = set(left)
        sright = set(right)
        # shove the common value to the countprio function
        key, = sleft & sright
        pt1prio += countprio(key)
print("Part 1:",pt1prio)

# part 2
pt2prio = 0
with open ('input', 'r') as file:
    # part 2 is a bit different since we need to compare each 3 lines but basically the same except we traverse the lines char by char instead of using the above set()
    data = [line for line in file]
    i = 0
    while i < len(data):
        for key in data[i]:
            if key in data[i+1] and key in data[i+2]:
                pt2prio += countprio(key)
                break
        i += 3
print("Part 2:",pt2prio)
