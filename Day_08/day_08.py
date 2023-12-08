import math

# read in the data
with open("r_08_input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

# inits
paths = {}
instructions = lines[0]
starts = [] # part 2

# for each path, create the L/R mapping
for x in lines[2:]:
    data = x.split(" = ")
    point = data[0]

    # fun string parsing
    lr_points = data[1].split(", ")
    l_point = lr_points[0].strip("(")
    r_point = lr_points[1].strip(")")

    # create map
    paths[point] = {"L": l_point, "R": r_point}

    # part 2 starts
    if point[-1] == "A":
        starts.append(point)

# PART 1:
count = 0
is_found = False

# start/end points
start = "AAA"
end = "ZZZ"

# loop until end of path
while not is_found:
    # for each L/R instruction
    for i in range(len(instructions)):
        # get next path
        ins = instructions[i]
        start = paths[start][ins]
        count += 1 # increment count

        # check if end of path
        if start == end:
            is_found = True
            break

print(f"PART 1: {count}")

# PART 2
steps = []

# for each starting point
for start in starts:
    # inits
    count = 0
    is_found = False

    # loop until end of path
    while not is_found:
        # for each L/R instruction
        for i in range(len(instructions)):
            # get next path
            ins = instructions[i]
            start = paths[start][ins]
            count += 1 # increment count

            # check if end of path (last letter Z)
            if start[-1] == "Z":
                is_found = True
                break

    # keep track of counts
    steps.append(count)

# LCM of counts
part2_counts = math.lcm(*steps)
print(f"PART 2: {part2_counts}")
