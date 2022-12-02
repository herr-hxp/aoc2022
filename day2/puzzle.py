# points
win = 6
draw = 3
rock = 1
paper = 2
scissors = 3
totalpoints = 0
totalpointsparttwo = 0

# move comparison
def rps(moves):
    # split moves into 2 items in a list
    moves = moves.split()
    #print(moves)
    # set the elf and player move from the list
    elf_move = moves[0]
    player_move = moves[1]
    # initiate a new round score
    roundscore = 0

    # start comparing the moves against each other
    match player_move:
        case "X": # rock
            roundscore += rock
            if elf_move == "A": # rock
                roundscore += draw
            elif elf_move == "C": # scissors
                roundscore += win
        case "Y": # paper
            roundscore += paper
            if elf_move == "A": # rock
                roundscore += win
            elif elf_move == "B": # paper
                roundscore += draw
        case "Z": # scissors
            roundscore += scissors
            if elf_move == "B": # paper
                roundscore += win
            elif elf_move == "C": # scissors
                roundscore += draw
    # send back the score of the round
    return roundscore

def parttwo(moves):
    # split moves into 2 items in a list
    moves = moves.split()
    #print(moves)
    # set the elf move and outcome from the list
    elf_move = moves[0]
    outcome = moves[1]
    # initiate a new round score
    roundscore = 0

    # find out which shape I need to chose
    match outcome:
        case "X": # I need to lose
            if elf_move == "A":
                player_move = "Z"
            elif elf_move == "B":
                player_move = "X"
            elif elf_move == "C":
                player_move = "Y"
        case "Y": # I need a draw
            if elf_move == "A":
                player_move = "X"
            elif elf_move == "B":
                player_move = "Y"
            elif elf_move == "C":
                player_move = "Z"
        case "Z": # I need to win
            if elf_move == "A":
                player_move = "Y"
            elif elf_move == "B":
                player_move = "Z"
            elif elf_move == "C":
                player_move = "X"

    # start comparing the moves against each other
    match player_move:
        case "X": # rock
            roundscore += rock
            if elf_move == "A": # rock
                roundscore += draw
            elif elf_move == "C": # scissors
                roundscore += win
        case "Y": # paper
            roundscore += paper
            if elf_move == "A": # rock
                roundscore += win
            elif elf_move == "B": # paper
                roundscore += draw
        case "Z": # scissors
            roundscore += scissors
            if elf_move == "B": # paper
                roundscore += win
            elif elf_move == "C": # scissors
                roundscore += draw
    # send back the score of the round
    return roundscore

# open the input file 
with open ('input' , 'r') as file:
    # remove the newlines
    data = [x.rstrip() for x in file]
    # send each line to the game function above and add the returned roundscore to the totalpoints
    for line in data:
        totalpoints += rps(line)
        totalpointsparttwo += parttwo(line)

# part 1
print("Part 1 - The total amount of points:",totalpoints)

# part 2
print ("Part 2 - The total amount of points:",totalpointsparttwo)
