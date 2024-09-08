"""

Doesnt work




"""



# Helper function to check if a cell is within the bounds of the grid
def is_within_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

# Function to extract a complete number from the grid starting at (r, c) and going in the specified direction
def extract_number(grid, r, c, rows, cols, dr, dc):
    number = ""
    while is_within_bounds(r, c, rows, cols) and grid[r][c].isdigit():
        number += grid[r][c]
        r += dr  # Move in the direction of dr (row direction)
        c += dc  # Move in the direction of dc (column direction)
        print (number)
    return int(number) if number else None

# Function to find the sum of all gear ratios in the schematic
def sum_gear_ratios(schematic):
    # Convert the schematic into a 2D grid
    grid = [list(line) for line in schematic.strip().splitlines()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Possible directions to check adjacent cells (8 directions: horizontal, vertical, and diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),         (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    
    total_gear_ratio_sum = 0
    
    # Iterate through the grid to find all gears (* symbols)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '*':  # Found a gear
                part_numbers = []

                print(part_numbers)
                
                # Check all adjacent cells for part numbers
                for dr, dc in directions:
                    adj_r = r + dr
                    adj_c = c + dc
                    if is_within_bounds(adj_r, adj_c, rows, cols):
                        # Extract the full number in the direction of (dr, dc)
                        number = extract_number(grid, adj_r, adj_c, rows, cols, dr, dc)
                        print (number)
                        if number is not None:
                            part_numbers.append(number)
                
                # If exactly two part numbers are found, calculate the gear ratio
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total_gear_ratio_sum += gear_ratio
    
    return total_gear_ratio_sum

# Example schematic input
schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# Calculate and print the sum of the gear ratios
print(sum_gear_ratios(schematic))  # Expected output: 467835
