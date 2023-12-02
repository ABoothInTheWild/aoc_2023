import numpy as np

# Read in Data
with open("02_input.txt") as f:
    data = f.readlines()

# inits
criteria = {"red":12, "green":13, "blue":14}
total = 0
total_power = 0

# for each row
for row in data:
    game = int(row.split(":")[0].split(" ")[1]) # parse the game id

    # get samples as a list
    samples = row.split(": ")[1].split("; ")
    samples = [x.strip() for x in samples]

    # init failure bool
    game_fail = False

    # init max per color for game
    game_max = {"red": 0, "green": 0, "blue": 0}

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

            # if val is new max, store it
            if val > game_max[color]:
                game_max[color] = val

    # if game succeeds, add to total
    if not game_fail:
        total += game

    # calculate game "power" by multiplying them all together
    game_power = np.prod(np.array(list(game_max.values())))
    total_power += game_power

print(f"Part 1: {total}")
print(f"Part 2: {total_power}")
