import re # idk if I need this here or not

def is_part_number(number, line_number, schematic_array):
    """
    number: A string containing the number to check
    line_number: (Integer) where the above number occurs
    schematic_lines: (List of strings) The schematic 
    """
    schematic_line = ''.join(schematic_array[line_number,])

    # Error checking 
    if len(re.findall("(?<!\d){number}(?!\d)", schematic_line)) > 1:
        print(f"Oh no! The regex looking for {number} matched more than once on line {line_number}")

    # Find the number, making sure it is not preceded or followed by a digit (so that if 
    # if number is '12', don't match '123').
    number_search = re.search(f"(?<!\d){number}(?!\d)", schematic_line)
    jmin, jmax = number_search.span()

    # Get the coordinates of the chars I need to search
    if line_number > 0 and line_number < schematic_array.shape[0] - 1 and jmin > 0 and jmax < len(schematic_line):
        to_search = [(i, j) for i in (line_number - 1, line_number + 1) for j in range(jmin - 1, jmax + 1)]
        to_search.append((line_number, jmin - 1))
        to_search.append((line_number, jmax))
    # The four horsemen of the apocalypse
    elif line_number == 0:
        to_search = [(line_number + 1, j) for j in range(jmin - 1, jmax + 1)]
        to_search.append((line_number, jmin - 1))
        to_search.append((line_number, jmax))
    elif line_number == schematic_array.shape[0] - 1:
        to_search = [(line_number - 1, j) for j in range(jmin - 1, jmax + 1)]
        to_search.append((line_number, jmin - 1))
        to_search.append((line_number, jmax))
    elif jmin == 0:
        to_search = [(i, j) for i in (line_number - 1, line_number + 1) for j in range(jmin, jmax + 1)]
        to_search.append((line_number, jmin))
        to_search.append((line_number, jmax))
    elif jmax == len(schematic_line):
        to_search = [(i, j) for i in (line_number - 1, line_number + 1) for j in range(jmin - 1, jmax)]
        to_search.append((line_number, jmin - 1))
        to_search.append((line_number, jmax - 1))
    else:
        print("I must've done sthg terribly wrong if you're seeing this")
        print(f"Number: {number}, line number: {line_number}")
        return()
    
    check_chars = [schematic_array[i, j] for i, j in to_search]
    if (all([re.search("[\.\d]", char) for char in check_chars])):
        return(False)
    else:
        return(True)