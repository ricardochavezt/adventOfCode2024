import sys

part2 = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--part2":
        part2 = True

operations_matrix_cache = {}

def generate_operations_matrix(cols):
    if cols in operations_matrix_cache:
        return operations_matrix_cache[cols]

    if part2:
        matrix = [["+"], ["*"], ["||"]]
    else:
        matrix = [["+"], ["*"]]
    for _ in range(cols-1):
        rows = len(matrix)
        for _ in range(rows):
            elem = matrix.pop(0)
            matrix.append(elem + ["+"])
            matrix.append(elem + ["*"])
            if part2:
                matrix.append(elem + ["||"])
    operations_matrix_cache[cols] = matrix
    return matrix

total = 0
valid_lines = []
invalid_lines = []
for line in sys.stdin:
    equation = line.strip().split()
    test_value = int(equation[0][:-1])
    operands = [int(op) for op in equation[1:]]

    operations = generate_operations_matrix(len(operands)-1)
    for operation_list in operations:
        acum = operands[0]
        for i in range(1, len(operands)):
            if operation_list[i-1] == "||":
                acum = (acum * (10 ** len(str(operands[i])))) + operands[i]
            elif operation_list[i-1] == "+":
                acum = acum + operands[i]
            else:
                acum = acum * operands[i]
        if acum == test_value:
            total += test_value
            break

print("Total:", total)
if not part2:
    print("(Run with --part2 for part 2 calculations)")
    print("(Might take considerably longer)")