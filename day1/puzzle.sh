#!/usr/bin/env bash

sum=0
sumlist=()

while IFS= read -r line
do
  if [[ $line =~ ^[0-9]+$ ]]; then
    sum=$((sum + line))
  else
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
