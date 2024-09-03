import re

'''
lines = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]

'''

lines = []

with open("cal_doc.txt", "r") as f:
    lines = f.readlines()    

# Strings zu Digits 
number_words_to_digits = {
    "zero": "0", "one": "1", "two": "2", "three": "3", 
    "four": "4", "five": "5", "six": "6", "seven": "7", 
    "eight": "8", "nine": "9"
}

def extract_calibration_value(line):
    calibration_value = 0

    # Find all numbers and number words in the line
    pattern = re.compile(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)', re.IGNORECASE)
    matches = pattern.findall(line)
    print(matches)
    # Convert words to numbers
    digits = []
    for match in matches:
        if match.lower() in number_words_to_digits:
            digits.append(number_words_to_digits[match.lower()])
        else:
            digits.append(match)

    # If there are at least two digits, return the first and last
    if len(digits) > 1:
        calibration_value = int(digits[0] + digits[-1])

    print(calibration_value)
    return calibration_value

def calculate_total_calibration_value(lines):

    total_calibration_value = 0
    for line in lines:
        total_calibration_value += extract_calibration_value(line)
        print(line) 
    return total_calibration_value




total = calculate_total_calibration_value(lines)
print("Total calibration value:", total)

