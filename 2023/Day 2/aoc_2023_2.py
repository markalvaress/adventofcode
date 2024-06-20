import re

games_file = open("input.txt", "r")
games = games_file.read()
games_file.close()

games_list = games.split("\n")

# Pt 1 ---------------------------------------
max_red, max_green, max_blue = (12, 13, 14)

def game_is_possible(game, max_red, max_green, max_blue):
    """
    Expects game to be ...
    """
    # Take out the game number and splits into runs
    game_runs = re.sub("Game \d+: ", "", game).split(";")

    for run in game_runs:
        # Loop over the 3 results within a run
        for colour_result in run.split(","):
            num_of_cubes = int(re.search("\d+", colour_result).group(0))

            if re.search("red", colour_result) and num_of_cubes > max_red:
                return False                
            elif re.search("green", colour_result) and num_of_cubes > max_green:
                return False 
            elif re.search("blue", colour_result) and num_of_cubes > max_blue:
                return False 
            
    return True


id_sum = 0
# Last item in list is blank
for game in games_list[:-1]:
    game_number = int(re.search("\d+", game).group(0))

    if game_is_possible(game, max_red, max_green, max_blue):
        print(game)
        print(f'Game {game_number} is possible')
        id_sum += game_number

id_sum

# Pt 2 -------------------------------------
game = games_list[0]

def min_cubes_required(game):
    game_runs = re.sub("Game \d+: ", "", game).split(";")
    r, g, b = ([], [], [])

    for run in game_runs:
        # Loop over the 3 results within a run and add the results to the relevant list
        for colour_result in run.split(","):
            num_of_cubes = int(re.search("\d+", colour_result).group(0))

            if re.search("red", colour_result):
                r.append(num_of_cubes)     
            elif re.search("green", colour_result):
                g.append(num_of_cubes)  
            elif re.search("blue", colour_result):
                b.append(num_of_cubes)  

    return (max(r), max(g), max(b))

powers = []

for game in games_list[:-1]:
    mcr = min_cubes_required(game)

    result = 1
    for num in mcr:
        result *= num

    powers.append(result)

sum(powers) #boshhhhhhhhhhhhhhhhhhhhhhh