import numpy as np

def findMove(pipe, last_move):
    """
    pipe: A char
    last_move: an np.array e.g. (0,1) for moving right
    """
    match pipe:
        case "F":
            if all(last_move == np.array([-1, 0])):
                next_move = np.array([0, 1])
            elif all(last_move == np.array([0, -1])):
                next_move = np.array([1, 0])
            else:
                print("Error: pipe doesn't connect")
                return
            
        case "7":
            if all(last_move == np.array([-1, 0])):
                next_move = np.array([0, -1])
            elif all(last_move == np.array([0, 1])):
                next_move = np.array([1, 0])
            else:
                print("Error: pipe doesn't connect")
                return
            
        case "J":
            if all(last_move == np.array([1, 0])):
                next_move = np.array([0, -1])
            elif all(last_move == np.array([0, 1])):
                next_move = np.array([-1, 0])
            else:
                print("Error: pipe doesn't connect")
                return
            
        case "L":
            if all(last_move == np.array([1, 0])):
                next_move = np.array([0, 1])
            elif all(last_move == np.array([0, -1])):
                next_move = np.array([-1, 0])
            else:
                print("Error: pipe doesn't connect")
                return
            
        case "|":
            if all(last_move == np.array([1, 0])):
                next_move = np.array([1, 0])
            elif all(last_move == np.array([-1, 0])):
                next_move = np.array([-1, 0])
            else:
                print("Error: pipe doesn't connect")
                return
            
        case "-":
            if all(last_move == np.array([0, 1])):
                next_move = np.array([0, 1])
            elif all(last_move == np.array([0, -1])):
                next_move = np.array([0, -1])
            else:
                print("Error: pipe doesn't connect")
                return
            
    return next_move 
        