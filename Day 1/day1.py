import re


file_name = "input.txt"

# read each line
with open(file_name, 'r') as file:
    output = 0
    numbers_str = ""
    for file_line in file:
        numbers = re.findall(r'\d+', file_line)
        output = output + int(numbers[0][0] + numbers[-1][-1])
    print(output)
    
