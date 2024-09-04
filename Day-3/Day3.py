schematic = ''

with open('input.txt', 'r') as f:
    schematic = f.read()


# check if the coordinates are in grid 
def is_within_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols



def sum_part_numbers(schematic):
    # Convert the schematic into a 2D grid
    grid = [list(line) for line in schematic.strip().splitlines()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Possible adjacent directions (8 directions including diagonals, structure of list just for visualization)
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),           (0, 1), 
                  (1, -1),  (1, 0),  (1, 1)]
    
    part_number_sum = 0
    
    # Iterate through each row in the grid
    for r in range(rows):
        c = 0
        while c < cols:
            # Identify complete number
            if grid[r][c].isdigit():
                # Extract full number
                start_c = c
                while c < cols and grid[r][c].isdigit():
                    c += 1
                number = int("".join(grid[r][start_c:c]))  # Convert the full number to an integer
                
                # is number adjacent to a symbol
                is_part_number = False
                for i in range(start_c, c):  # Check adjacent cells for each digit in the number
                    for dr, dc in directions:
                        adj_r = r + dr
                        adj_c = i + dc
                        if is_within_bounds(adj_r, adj_c, rows, cols):
                            if grid[adj_r][adj_c] not in ('.', ' ') and not grid[adj_r][adj_c].isdigit():
                                is_part_number = True
                                break
                    if is_part_number:
                        break
                
                # If part number  add its value to the sum
                if is_part_number:
                    part_number_sum += number
            else:
                c += 1
    
    return part_number_sum



print(sum_part_numbers(schematic))

