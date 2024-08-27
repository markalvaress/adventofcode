import re

def get_path_length(nci_dict, instructions):
    current_node = 'AAA'
    path_length = 0

    while current_node != 'ZZZ':
        children = re.findall("\w{3}", nci_dict[current_node])
        next_step = instructions[path_length % len(instructions)]
        if next_step == 'L':
            current_node = children[0]
        else:
            current_node = children[1]
        
        path_length += 1

    return path_length        


def get_path_length2(nci_dict, instructions, start_node):
    current_node = start_node
    path_length = 0

    while not re.search("Z$", current_node):
        children = re.findall("\w{3}", nci_dict[current_node])
        next_step = instructions[path_length % len(instructions)]
        if next_step == 'L':
            current_node = children[0]
        else:
            current_node = children[1]
        
        path_length += 1

    return path_length 

# Graveyard ---------------------------------------------------

# The hope here was that I could've added a method to traverse the tree, but in the end I didn't really need this object
# because I can do everything I need with the dictionary
class BinaryTree:
    def __init__(self, value, split_ncis):
        self.value = value
        children = re.findall("\w{3}", split_ncis[value])
        if self.value != children[0]:
            self.left = BinaryTree(children[0], split_ncis) # python passes split_ncis by reference so don't have to worry about it being copied over lots of times
        if self.value != children[1]:
            self.right = BinaryTree(children[1], split_ncis)

        return