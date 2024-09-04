


lines = []

with open("cal_doc.txt", "r") as f:
    lines = f.readlines()    

# Strings to Digits 
number_words_to_digits = {
    "zero": "0", "one": "1", "two": "2", "three": "3", 
    "four": "4", "five": "5", "six": "6", "seven": "7", 
    "eight": "8", "nine": "9"
}

def extract_calibration_value(line):
    calibration_value = 0
    digits = []
    i = 0 


    while i < len(line):
        found = False
        for word, digit in number_words_to_digits.items():
            if line[i:i+len(word)].lower() == word:
                digits.append(digit)
                i += len(word) -1  # catches cases like "twone" "fiveight" etc
                found = True
                break
        if not found: 
            if line[i].isdigit():
                digits.append(line[i])
            i += 1

    if len(digits) > 1:
        calibration_value = int(digits[0] + digits[-1])
    

    elif len(digits) == 1:
        calibration_value = int(digits[0] + digits[0])    

    print(f"Calibration value for '{line}':", calibration_value)
    return calibration_value


def calculate_total_calibration_value(lines):
    total_calibration_value = 0
    for index, line in enumerate(lines, start=1):
        print(f"Line {index}: {line}")
        total_calibration_value += extract_calibration_value(line)
    return total_calibration_value

# Calculating total calibration value
total = calculate_total_calibration_value(lines)
print("Total calibration value:", total)

  