# Okay want to find the length of the loop starting at S and then just divide that by two?
import numpy as np
import re
from helpers import findMove

f = open("input.txt")
contents = f.read()
f.close()

map = contents.splitlines()

# find the starting point
for row_start in range(len(map)):
    col_start = map[row_start].find("S")
    if col_start != -1:
        break

# by inspection I see that we can start going up
last_move = np.array([-1, 0])
current_loc = np.array([row_start, col_start]) + last_move
pipe_length = 1

while map[current_loc[0]][current_loc[1]] != "S":
    current_pipe = map[current_loc[0]][current_loc[1]]
    next_move = findMove(current_pipe, last_move)
    current_loc += next_move
    last_move = next_move # this is to make it easier to read - i could've just done last_move = findMove(...) above
    pipe_length += 1
    #print(map[current_loc[0]][current_loc[1]]) # if you want to see what's going on

furthest_dist = pipe_length / 2

# pt 2

# Given I've found the main pipe, I want to find the number of elements enclosed in that pipe (essentially the area of the shape of which the pipe is a border)

# F-----7
# |.....|
# |.....|
# L-----J