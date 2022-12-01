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

# set the first item in the list to the largest number and compare the rest, if it's bigger we make the variable reflect the new number
max = sumlist[0]
for num in sumlist:
    if num > max:
        max = num

# print out the biggest number we could find in the list
print("The elf carrying the most has a total of:",max)
