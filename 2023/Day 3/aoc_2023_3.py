import re
import numpy as np
from is_part_number import is_part_number

schematic_file = open("input.txt", "r")
schematic = schematic_file.read()
schematic_file.close()

schematic_lines = np.array(schematic.split("\n")[:-1])
schematic_array = np.array([list(line) for line in schematic_lines]) # in the end I don't think I needed this but I'm too deep now

result = 0
for line_num in range(len(schematic_lines)):
    numbers = re.findall("\d+", schematic_lines[line_num])

    for number in numbers:
        if is_part_number(number, line_num, schematic_array):
            result += int(number)

    
