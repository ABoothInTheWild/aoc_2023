from collections import defaultdict

# read in data
with open("03_input.txt") as f:
    data = f.readlines()

# inits
total = 0 # part 1
gears = defaultdict(list) # part 2, allows not having to check if key exists

# for each row
for i in range(len(data)):
    row = data[i]

    # want to build a number, reset these per row
    num = ""
    is_valid = False
    found_chars = []

    # for each char in row
    for j in range(len(row)):
        # coords to check for symbols
        vals = [[i-1, j-1], [i-1, j], [i-1, j+1],
               [i, j-1], [i, j+1],
               [i+1, j-1], [i+1, j], [i+1, j+1]]

        char = row[j]

        # if it's a digit, need to check for symbols
        if char.isdigit():
            num += char # build number

            # if the symbol hasn't been found
            if not is_valid:
                # for each coord to check
                for indx in vals:
                    x = indx[0]
                    y = indx[1]

                    # if x in range, and y in range
                    if (x in range(len(data))) & (y in range(len(row))):
                        # pull the coord value and check if valid
                        symbol = data[x][y].strip()
                        if (symbol not in '.0123456789'):
                            is_valid = True

                            # for part 2 - store the found symbol in a list
                            info = {"symbol": symbol, "coords": f"{x}_{y}"}
                            found_chars.append(info)

        else:
            # if not a digit, check if we found a part number
            if (len(num) > 0) & (is_valid):
                total += int(num)

                # find gears from found symbols
                for info in found_chars:
                    if info["symbol"] == "*":
                        gears[info["coords"]].append(num)

            # reset for the next number on the row
            num = ""
            is_valid = False
            found_chars = []

# Part 1
print(f"Part 1: {total}")

# Part 2
gear_total = 0
for gear, val in gears.items():
    if len(val) >= 2:
        gear_total += int(val[0])*int(val[1])

print(f"Part 2: {gear_total}")
