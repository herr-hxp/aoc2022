pt1counter = 0
pt2counter = 0

with open ('input', 'r') as file:
    data = [x.rstrip() for x in file]
    for line in data:
        first_elf, second_elf = line.split(',')
        first_start, first_end = [int(x) for x in first_elf.split('-')]
        second_start, second_end = [int(x) for x in second_elf.split('-')]

        # part 1
        if first_start <= second_start <= first_end and first_start <= second_end <= first_end:
            pt1counter += 1
        elif second_start <= first_start <= second_end and second_start <= first_end <= second_end:
            pt1counter += 1

        # part 2
        if first_start <= second_start <= first_end or first_start <= second_end <= first_end:
            pt2counter += 1
        elif second_start <= first_start <= second_end or second_start <= first_end <= second_end:
            pt2counter += 1

print("Part 1:", pt1counter)
print("Part 2:", pt2counter)
