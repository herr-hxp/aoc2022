# debug flag
DEBUG=0

# our five elfs
elf_one = [1000, 2000, 3000]
elf_two = [4000]
elf_three = [5000, 6000]
elf_four = [7000, 8000, 9000]
elf_five = [10000]

# elf baked into one list
elf_list = [elf_one, elf_two, elf_three, elf_four, elf_five]

# debug function
def debug(str):
    if DEBUG:
        print(str)

def endmsg(num):
    print("The elf with the most calories is carrying:",num)

# add together each elf's total calories
res = list(map(sum, elf_list))
debug(res)

# find the largest number in the result above
max = res[0]
for i in range(0,len(res)):
    if res[i] > max:
        max = res[i]

endmsg(max)
