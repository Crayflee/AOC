scratchcards = []

with open("cards.txt") as f:
    scratchcards = [line.strip() for line in f.readlines()]




def calculate_card_points(winning_numbers, nums_to_check):
    matches = 0  
    points = 0  

    # Convert the lists to sets to check for matches
    winning_set = set(winning_numbers)
    for num in nums_to_check:
        if num in winning_set:
            matches += 1
            if matches == 1:
                points += 1  # First match gives 1 point
            else:
                points *= 2  # Each subsequent match doubles the points

    return points


def calculate_total_points(scratchcards):
    total_points = 0

    # Process each card
    for card in scratchcards:
        parts = card.split(":")[1].strip()  
        winning_part, nums_to_check_part = parts.split("|")  # Split by the pipe character

        # Convert the space-separated parts to lists of integers
        winning_numbers = list(map(int, winning_part.split()))
        nums_to_check = list(map(int, nums_to_check_part.split()))

        total_points += calculate_card_points(winning_numbers, nums_to_check)

    return total_points



total_points = calculate_total_points(scratchcards)
print("Total points:", total_points)  


