#!/usr/bin/env bash

# initialize sum to 0 and create an empty array
sum=0
sumlist=()

# read each line of the input file
while IFS= read -r line
do
  # check if the line is all digits
  if [[ $line =~ ^[0-9]+$ ]]; then
    # add the line to the sum
    sum=$((sum + line))
  else
    # line is not all digits, so append the current sum to the sumlist
    # array and reset the sum to 0
    sumlist+=("$sum")
    sum=0
  fi
done < input

# sort the array in descending order
mapfile -t sorted < <(printf '%s\n' "${sumlist[@]}" | sort -rn)

# print out the biggest sum
echo "The elf carrying the most has a total of: ${sorted[0]}"

# add the three biggest sums together
newsum=$((sorted[0] + sorted[1] + sorted[2]))
echo "The three elfs carrying the most has a total of: $newsum"
