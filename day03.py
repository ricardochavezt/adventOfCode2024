import re
import fileinput

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

sum = 0
conditional_sum = 0
instructions_enabled = True
for line in fileinput.input():
    for instruction_match in pattern.finditer(line.strip()):
        if instruction_match[0] == "do()":
            instructions_enabled = True
        elif instruction_match[0] == "don't()":
            instructions_enabled = False
        else:
            operands = instruction_match.group(1, 2)
            result = int(operands[0]) * int(operands[1])
            sum += result
            if instructions_enabled:
                conditional_sum += result

print("Total sum: ", sum)
print("Conditional sum:", conditional_sum)