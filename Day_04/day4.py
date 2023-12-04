from aoc_helper import extract_ints
from collections import defaultdict

with open("04_input.txt") as f:
    data = f.readlines()

## PART 1

# init points
total = 0

# for each row
for row in data:
    # extract winning numbers and our numbers
    row = row.split(": ")[1].split(" | ")
    winning_numbers = extract_ints(row[0])
    our_nums = extract_ints(row[1])

    # set intersection for overlap
    cards = list(set(our_nums).intersection(winning_numbers))

    # init points
    points = 0
    if len(cards) > 0:
        # double points for each card match
        points += 2**(len(cards)-1)

    # add to total
    total += points

print(f"PART 1: {total}")

## PART 2
card_wins = defaultdict(int)

# for each row (indexed)
for i in range(len(data)):
    # extract winning numbers and our numbers
    row = data[i].split(": ")[1].split(" | ")
    winning_numbers = extract_ints(row[0])
    our_nums = extract_ints(row[1])

    # set intersection for overlap
    cards = list(set(our_nums).intersection(winning_numbers))

    # add one win to our card to account for original
    card_wins[i] += 1
    if len(cards) > 0:
        # for each match
        for j in range(len(cards)):
            # add the number of cards to the new card
            # the 1 + j is sketch, but for only one match,
            # need to add 1 to the next card, and looping
            # range(1, len(cards)-1) doesn't work
            card_wins[i+1+j] += card_wins[i]

total2 = sum(card_wins.values())
print(f"PART 2: {total2}")
