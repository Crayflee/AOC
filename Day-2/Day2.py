import re
from math import prod

'''
games = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]
'''

games = []

with open("games.txt", "r") as f:
    games = f.readlines()

def parse_game(game_str):
    
    #Parse a game string and return the minimum required cube counts for each color.
    
    rounds = game_str.split(";")
    min_red_cubes, min_green_cubes, min_blue_cubes = 0, 0, 0
    pattern = re.compile(r'(\d+)\s(red|green|blue)')

    for rnd in rounds:
        red_cubes, green_cubes, blue_cubes = 0, 0, 0
        matches = pattern.findall(rnd.strip())

        for num, color in matches:
            num = int(num)
            if color == 'red':
                red_cubes += num
            elif color == 'green':
                green_cubes += num
            elif color == 'blue':
                blue_cubes += num

        min_red_cubes = max(min_red_cubes, red_cubes)
        min_green_cubes = max(min_green_cubes, green_cubes)
        min_blue_cubes = max(min_blue_cubes, blue_cubes)

    return min_red_cubes, min_green_cubes, min_blue_cubes

def calculate_power(min_cube_counts):
    #Calculate the power of a set of cube counts by computing their product.
    return prod(min_cube_counts)

def solve(games):
    total_power = 0

    for game in games:
        name, details = game.split(":")
        red_cubes, green_cubes, blue_cubes = parse_game(details.strip())
        total_power += calculate_power([red_cubes, green_cubes, blue_cubes])

    return total_power



# Solve the problem
result = solve(games)
print("Total power:", result)
