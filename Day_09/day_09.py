# Imports
import pandas as pd
from aoc_helper import extract_ints

# read in data
with open("r_09_input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

lines = [extract_ints(x) for x in lines]

# init totals for both parts
total1 = 0
total2 = 0

# for each line, we'll create a DF using .diff() until the column is all zeros
for line in lines:
    # first column
    sub = pd.Series(line)
    cols = [sub] # init list of "diff"-ed columns

    # start loop
    new = sub.copy()
    is_zero = (new.fillna(0) == 0).all() # can't just sum = 0 as I found out..

    while not is_zero:
        new = new.diff() # new diffed column
        cols.append(new)
        is_zero = (new.fillna(0) == 0).all() # check if col is all zero

    # final df of init to all zero columns
    df = pd.DataFrame(cols).T

    # inits
    first_row = [] # Part 2
    last_row = [] # Part 1
    cols = list(df.columns)[::-1] # reversed

    # for each column
    for x in range(len(cols)):
        col = cols[x]

        # if last column, then val is 0 by definition
        if col == cols[0]:
            last_val = 0
            first_val = 0
        else:
            # val is the last/first valid row of the column +/- the last found val
            last_val = df.iloc[-1, col] + last_val
            first_val = df.iloc[df[col].first_valid_index(), col] - first_val

        # append to found values
        last_row.append(last_val)
        first_row.append(first_val)

    # un-reverse
    last_row = last_row[::-1]
    first_row = first_row[::-1]

    # insert into df
    df.loc[len(df.index)] = last_row

    # hack to get first row first
    df.loc[-1] = first_row
    df.index = df.index + 1  # shifting index
    df.sort_index(inplace=True)

    # get the final value and add to total
    final1 = df.iloc[-1, 0]
    total1 += final1

    final2 = df.iloc[0, 0]
    total2 += final2

print(f"PART 1: {total1}")
print(f"PART 2: {total2}")
