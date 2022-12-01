with open('input', 'r') as file:
    # put the lines in a list, and strip the pesky newlines
    elflist = [x.rstrip() for x in file]
    # create a sum var and a sum list to put the sums in
    sum = 0
    sumlist = []
    # go through our list and check if the line is an integer, then add it to the sum,
    # if not, append the sum to the list of sums and start summing up the next part
    for line in elflist:
        if line.isdigit():
            sum = sum+int(line)
        else:
            sumlist.append(sum)
            sum = 0

# sort the list of sums in reverse order
sumlist.sort(reverse=True)

# part 1
# print out the biggest sum
print("The elf carrying the most has a total of:",sumlist[0])

# part 2
# add the three biggest sums together
newsum = sumlist[0] + sumlist[1] + sumlist[2]
print("The three elfs carrying the most has a total of:",newsum)
