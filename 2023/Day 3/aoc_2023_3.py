import re
import numpy as np
from helpers import is_part_number, ratio_if_gear

schematic_file = open("input.txt", "r")
schematic = schematic_file.read()
schematic_file.close()

schematic_lines = np.array(schematic.split("\n")[:-1])
schematic_array = np.array([list(line) for line in schematic_lines]) # in the end I don't think I needed this but I'm too deep now

# pt 1
result = 0
for line_num in range(len(schematic_lines)):
    numbers = re.findall("\d+", schematic_lines[line_num])

    for number in numbers:
        if is_part_number(number, line_num, schematic_array):
            result += int(number)


# pt 2

# get a list of lists of numbers found on each line of schematic_lines (need to unpack the result of re.finditer())
number_search_results = [re.finditer("\d+", schematic_lines[i]) for i in range(len(schematic_lines))]
number_search_results_unpacked = []
for results in number_search_results:
    number_search_results_unpacked.append([number for number in results])

star_search_results = [re.finditer("\*", schematic_lines[i]) for i in range(len(schematic_lines))]

gear_ratio_sum = 0

for i in range(len(star_search_results)):
    print(f"line number: {i}")
    for star_match in star_search_results[i]:
        if i == 0:
            gear_ratio_sum += ratio_if_gear(star_match, number_search_results_unpacked[i:i+2]) # +2 because slicing doesn't include endpoint
        elif i == len(star_search_results) - 1:
            gear_ratio_sum += ratio_if_gear(star_match, number_search_results_unpacked[i-1:i+1])
        else:
            gear_ratio_sum += ratio_if_gear(star_match, number_search_results_unpacked[i-1:i+2])
        
