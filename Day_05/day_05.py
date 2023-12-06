from aoc_helper import extract_ints

# get text
with open("05_input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

# get seeds
seeds = extract_ints(lines[0])

# get collection of maps (list of lists)
maps = []
for row in lines[2:]:
    if "map" in row:
        sub = []
    elif row == "":
        maps.append(sub)
    else:
        sub.append(extract_ints(row))

# last line
maps.append(sub)

# create dict per seed, default to seed value
vals = {}
for seed in seeds:
    vals[seed] = seed

# for each seed
for seed in seeds:
    # for each map
    for inp_map in maps:
        # get value for seed
        val = vals[seed]
        for inp in inp_map:
            dest, source, range_len = inp[0], inp[1], inp[2]

            # calculate diff per input
            diff = dest - source
            if (val >= source) and (val < source + range_len):
                val = val + diff # if matches overwrite map
                break

        # save new mapped value
        vals[seed] = val

# get minimums
print(min(vals.values()))
