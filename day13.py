import fileinput
import re
from math import floor

button_a_re = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
button_b_re = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
prize_re = re.compile(r"Prize: X=(\d+), Y=(\d+)")

def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def solve_equation_system(coefficient_matrix, constant_matrix):
    # The algorithm goes this way:
    # - Calculate the inverse of the coefficients matrix
    # If M = [a, b], the inverse of M (M^-1) = 1/determinant * [d, -b]
    #        [c, d]                                            [-c, a]
    # - Multiply the inverse of the coefficients matrix with the constants matrix
    # The result has the solutions for the system
    det = determinant(coefficient_matrix)
    if det == 0: # system has either no solutions or infinite solutions
        return None
    
    inverse_matrix = [[coefficient_matrix[1][1], -coefficient_matrix[0][1]],
                      [-coefficient_matrix[1][0], coefficient_matrix[0][0]]]
    
    product_matrix = []
    for i in range(len(coefficient_matrix)):
        sum = 0
        for j in range(len(coefficient_matrix[i])):
            sum += (inverse_matrix[i][j] * constant_matrix[j][0])
        
        product_matrix.append([sum])

    for i in range(len(product_matrix)):
        for j in range(len(product_matrix[i])):
            product_matrix[i][j] /= det

    solutions = [x for xs in product_matrix for x in xs]
    return solutions

button_a_behavior = None
button_b_behavior = None
prize_coordinates = None

def try_find_solution(button_a_behavior, button_b_behavior, prize_coordinates, part2=False):
    coefficients = [[button_a_behavior[0], button_b_behavior[0]], [button_a_behavior[1], button_b_behavior[1]]]
    constants = [[x] for x in prize_coordinates]
    solution = solve_equation_system(coefficients, constants)
    # only integer solutions
    if solution and all([floor(s) == s for s in solution]):
        if part2 or all([s <= 100 for s in solution]):
            return solution[0] * 3 + solution[1]

    return 0

total_tokens = 0
total_tokens_part2 = 0
for line in fileinput.input():
    if (button_a_match := button_a_re.match(line.strip())):
        button_a_behavior = [int(button_a_match[1]), int(button_a_match[2])]
    elif (button_b_match := button_b_re.match(line.strip())):
        button_b_behavior = [int(button_b_match[1]), int(button_b_match[2])]
    elif (prize_match := prize_re.match(line.strip())):
        prize_coordinates = [int(prize_match[1]), int(prize_match[2])]
    else:
        if button_a_behavior and button_b_behavior and prize_coordinates:
            total_tokens += try_find_solution(button_a_behavior, button_b_behavior, prize_coordinates)
            total_tokens_part2 += try_find_solution(button_a_behavior, button_b_behavior, [c + 10**13 for c in prize_coordinates], part2=True)
            button_a_behavior = None
            button_b_behavior = None
            prize_coordinates = None

if button_a_behavior and button_b_behavior and prize_coordinates:
    total_tokens += try_find_solution(button_a_behavior, button_b_behavior, prize_coordinates)
    total_tokens_part2 += try_find_solution(button_a_behavior, button_b_behavior, [c + 10**13 for c in prize_coordinates], part2=True)

print("Total tokens spent:", total_tokens)
print("Total tokens spent (part 2):", total_tokens_part2)