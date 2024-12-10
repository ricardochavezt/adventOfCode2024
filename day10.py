import fileinput
import re

zero_re = re.compile("0")
current_level = []
topographic_map = []

def position_in_map(row, col):
    return (0 <= row < len(topographic_map)) and (0 <= col < len(topographic_map[row]))

def follow_new_level(row, col, level):
    next_steps = []
    for (d_row, d_col) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (position_in_map(row+d_row, col+d_col)
            and int(topographic_map[row+d_row][col+d_col]) == level):
            next_steps.append((row+d_row, col+d_col))

    return next_steps

for index, line in enumerate(fileinput.input()):
    topographic_map.append(line.strip())
    for match in zero_re.finditer(line.strip()):
        current_level.append([(index, match.start())])

for level in range(1, 10):
    new_level = []
    for position_list in current_level:
        new_position_list = []
        for (row, col) in position_list:
            new_position_list.extend(follow_new_level(row, col, level))
        
        new_level.append(new_position_list)

    current_level = new_level

sum_of_scores = sum([len(set(l)) for l in current_level])
print("Sum of scores:", sum_of_scores)
sum_of_ratings = sum([len(l) for l in current_level])
print("Sum of ratings:", sum_of_ratings)