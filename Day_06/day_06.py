from aoc_helper import extract_ints

# read in data
with open("06_input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

# get times/distances
times = extract_ints(lines[0])
distances = extract_ints(lines[1])

# inits
vals = list(zip(times, distances))
total = 1

# for each time length
for inp in vals:
    x = inp[0]
    count = 0

    # for each millisecond
    for i in range(x+1):
        # calculate distance
        dist = i * (len(range(x)) - i)
        if dist > inp[1]:
            count += 1

    # add to total
    total *= count

print(f"Part 1: {total}")

# get new times/distances
times = extract_ints(lines[0].replace(" ", ""))
distances = extract_ints(lines[1].replace(" ", ""))

# inits
vals = list(zip(times, distances))
total2 = 1

# for each time length
for inp in vals:
    x = inp[0]
    count = 0

    # for each millisecond
    for i in range(x+1):
        # calculate distance
        dist = i * (len(range(x)) - i)
        if dist > inp[1]:
            count += 1

    # add to new total
    total2 *= count

print(f"Part 2: {total2}")
