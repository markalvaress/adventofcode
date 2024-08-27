import re
import copy

sequences_file = open("2023/Day 9/input.txt", "r")
sequences = sequences_file.read().splitlines()
sequences_file.close()

sequences_split = [sequence.split(" ") for sequence in sequences]
for i, split_seq in enumerate(sequences_split):
    sequences_split[i] = [int(val) for val in split_seq]


def getDifferencesLists(sequence):
    differences = [sequence]
    j = 0

    while not all(diff == 0 for diff in differences[j]):
        differences.append([differences[j][i + 1] - differences[j][i] for i in range(len(differences[j]) - 1)])
        j += 1

    return differences

def extrapolate(differences_lists):
    diff_lists_local = copy.deepcopy(differences_lists) # so that changes made to the differences_list don't escape

    diff_lists_local[-1].append(0)
    for j in range(2, len(diff_lists_local) + 1):
        diff_lists_local[-j].append(diff_lists_local[-j][-1] + diff_lists_local[-j + 1][-1])

    return diff_lists_local[0][-1]

def getNextValue(sequence, direction = 'f'):
    """direction: 'f' for forward, 'b' (or anything else) for backwards."""
    differences_list = getDifferencesLists(sequence)
    if (direction == 'f'):
        next_value = extrapolate(differences_list)
    else:
        next_value = extrapolate_back(differences_list)
    
    return next_value

extrapolated_vals = [getNextValue(sequence) for sequence in sequences_split]
sum(extrapolated_vals)

# parte 2 ------------------------------------------------------------------------------------------------------
def extrapolate_back(differences_lists):
    diff_lists_local = copy.deepcopy(differences_lists) # so that changes made to the differences_list don't escape

    diff_lists_local[-1].insert(0, 0)
    for j in range(2, len(diff_lists_local) + 1):
        diff_lists_local[-j].insert(0, diff_lists_local[-j][0] - diff_lists_local[-j + 1][0])

    return diff_lists_local[0][0]

extrapolated_back_vals = [getNextValue(sequence, direction = 'topsy_turvy_back_to_front') for sequence in sequences_split]
sum(extrapolated_back_vals)