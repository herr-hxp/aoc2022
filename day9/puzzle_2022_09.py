from aocd import lines

# Define a function to compute the sign of a number
def sign(x):
    return (x > 0) - (x < 0)

# Initialize sets to store unique locations visited by the first and last point in the sequence
part1, part2 = set(), set()

# Initialize the sequence of points with 10 points at the origin (0 + 0j)
knot = [0 + 0j for _ in range(10)]

for motion in lines:
    # Repeat the motion a number of times equal to the numeric value after the initial letter
    for _ in range(int(motion[1:])):
        # Update the position of each point in the sequence
        for i in range(len(knot)):
            d = 0
            # If this is the first point in the sequence, move it according to the current motion
            if i <= 0:
                d = {"R": 1, "L": -1, "U": 1j, "D": -1j}[motion[0]]
            # If this is not the first point, move it relative to the previous point
            else:
                k = knot[i - 1] - knot[i]
                # If the distance between the previous and current point is at least 2, move the current point
                if abs(k) >= 2:
                    d = sign(k.real) + sign(k.imag) * 1j
            
            # Update the position of the current point
            knot[i] = knot[i] + d
            
            # Add the current location to the set of unique locations visited by the first and last point
            if i == 1: part1.add(knot[i])
            if i == 9: part2.add(knot[i])

# Print the number of unique locations visited by the first and last point in the sequence                
print("Part 1:", len(part1))
print("Part 2:", len(part2))
