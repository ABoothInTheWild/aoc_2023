import numpy as np

# Read in Data
with open("02_input.txt") as f:
    data = f.readlines()

# PART 1
criteria = {"red":12, "green":13, "blue":14}
total = 0

# for each row
for row in data:
    game = int(row.split(":")[0].split(" ")[1]) # parse the game id

    # get samples as a list
    samples = row.split(": ")[1].split("; ")
    samples = [x.strip() for x in samples]

    # init failure bool
    game_fail = False

    # for each color
    for color in criteria.keys():
        # for each sample
        for sample in samples:
            if color in sample:
                # get the value for that color
                val = int(sample.split(f" {color}")[0].split(" ")[-1])
            else:
                # color doesn't exist in sample, default to 0
                val = 0

            # check if color value is greater than threshold
            if val > criteria[color]:
                game_fail = True
                break # no need to check other samples

        if game_fail:
            break # no need to check other colors

    # if game succeeds, add to total
    if not game_fail:
#         print(row)
        total += game

print(f"Part 1: {total}")

#############################################
# Part 2 - get max per color per row

# inits
colors = ["red", "blue", "green"]
total = 0

# for each row
for row in data:
    game = int(row.split(":")[0].split(" ")[1]) # parse the game id

    # get samples as a list
    samples = row.split(": ")[1].split("; ")
    samples = [x.strip() for x in samples]

    # init max per color for game
    game_max = {"red": 0, "green": 0, "blue": 0}

    # for each color
    for color in colors:
        # for each sample
        for sample in samples:
            if color in sample:
                # get the value for that color
                val = int(sample.split(f" {color}")[0].split(" ")[-1])
            else:
                # color doesn't exist in sample, default to 0
                val = 0

            # if val is new max, store it
            if val > game_max[color]:
                game_max[color] = val

    # calculate game "power" by multiplying them all together
    game_power = np.prod(np.array(list(game_max.values())))

    # add to total
    total += game_power

print(f"Part 2: {total}")
