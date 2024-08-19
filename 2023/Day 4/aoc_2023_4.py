import re
import numpy as np
from helpers import num_matching

scratchcards_file = open("input.txt", "r")
scratchcards = scratchcards_file.read()
scratchcards_file.close()

scratchcards_lines = [re.sub("Card .*:", "", line) for line in scratchcards.splitlines()]

# Pt uno
scratchcard_points = 0
for card in scratchcards_lines:
    num_matching_nums = num_matching(card)
    if num_matching_nums != 0:
        scratchcard_points += 2**(num_matching_nums - 1)

# Pt dos
num_copies = np.ones(len(scratchcards_lines), dtype = int)

for i in range(len(scratchcards_lines)):
    x = num_matching(scratchcards_lines[i])
    num_copies[i+1:i+x+1] += num_copies[i]

sum(num_copies) #poggers