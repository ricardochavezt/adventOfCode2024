import re
import fileinput

pattern = re.compile("XMAS")
pattern_backwards = re.compile("SAMX")

count = 0
matrix = []
for line in fileinput.input():
    stripped_line = line.strip()
    count += len(pattern.findall(stripped_line))
    count += len(pattern_backwards.findall(stripped_line))
    matrix.append([stripped_line[i] for i in range(len(stripped_line))])

# transpose and count again
transpose = [['' for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
for i in range(len(transpose)):
    for j in range(len(transpose[i])):
        transpose [i][j] = matrix[j][i]

transposed_lines = ["".join(line) for line in transpose]
for line in transposed_lines:
    count += len(pattern.findall(line))
    count += len(pattern_backwards.findall(line))

# count diagonals
for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        for d_row, d_col in [(+1, +1), (-1, +1), (+1, -1), (-1, -1)]:
            found_diagonal = True
            for n, c in enumerate(["X", "M", "A", "S"]):
                i_check, j_check = i + n * d_row, j + n * d_col
                if i_check < 0 or i_check >= len(matrix):
                    found_diagonal = False
                    break
                if j_check < 0 or j_check >= len(row):
                    found_diagonal = False
                    break
                if matrix[i_check][j_check] != c:
                    found_diagonal = False
                    break
            
            if found_diagonal:
                count += 1

print("Total occurrences of XMAS:", count)

# count X-MAS
x_mas_count = 0
for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[i])-1):
        if matrix[i][j] == "A":
            diag1 = "".join([matrix[i-1][j-1], matrix[i][j], matrix[i+1][j+1]])
            diag2 = "".join([matrix[i-1][j+1], matrix[i][j], matrix[i+1][j-1]])

            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                x_mas_count += 1 

print("Total occurrences of X-MAS:", x_mas_count)