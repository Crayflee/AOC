lines =[]
with open("cal_doc.txt", "r") as f:
    lines = f.readlines()

def extract_calibration_value(line):
    first_digit = None
    last_digit = None
    
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    # letztes Zeichen
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    # wenn beide gefunden, kombinieren 
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    
    # wenn keine gefunden werden, 0 zurückgeben 
    return 0

def sum_calibration_values(lines):
    total_sum = 0
    for line in lines:
        total_sum += extract_calibration_value(line)
    return total_sum



total = sum_calibration_values(lines)
print("Total calibration value:", total)
