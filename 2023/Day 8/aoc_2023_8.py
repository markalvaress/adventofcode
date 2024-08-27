import re
from helpers import get_path_length, get_path_length2

map_file = open("2023/Day 8/input.txt", "r")
map = map_file.read()
map_file.close()

map_lines = map.splitlines()
instructions = map_lines[0]
network_creation_instructions = map_lines[2:len(map_lines)]
network_creation_instructions[len(network_creation_instructions) - 1]

split_ncis = [nci.split(" = ") for nci in network_creation_instructions]

split_ncis_dict = dict()
for split_nci in split_ncis:
    split_ncis_dict[split_nci[0]] = split_nci[1]

get_path_length(split_ncis_dict, instructions)

# pt 2
import math

nodes = [name for name, value in split_ncis_dict.items()]
start_nodes = []
for node in nodes:
    if re.search("A$", node):
        start_nodes.append(node)

path_lengths = [get_path_length2(split_ncis_dict, instructions, start_node) for start_node in start_nodes]
final_path_length_simul = math.lcm(*path_lengths)


# Code graveyard ------------------------------------------------------
#from helpers import BinaryTree

# Testing that it works as expected
# baby_dict = {'AAA': '(BBB, CCC)', 'BBB': '(DDD, EEE)', 'CCC': '(FFF, GGG)', 'DDD': '(DDD, DDD)', 'EEE': '(EEE, EEE)', 'FFF': '(FFF, FFF)', 'GGG': '(GGG, GGG)'}
# baby_map_tree = BinaryTree('AAA', baby_dict)

# This hits recursion depth :(
#map_tree = BinaryTree('AAA', split_ncis_dict)