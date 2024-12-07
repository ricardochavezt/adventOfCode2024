import fileinput

map = []
current_row, current_col = 0, 0
for row, line in enumerate(fileinput.input()):
    if (col := line.find("^")) != -1:
        current_row, current_col = row, col
    map.append(line.strip())

direction_row, direction_col = -1, 0

def rotate_90deg_right(direction_row, direction_col):
    match (direction_row, direction_col):
        case (-1, 0):
            return 0, 1
        case (0, 1):
            return 1, 0
        case (1, 0):
            return 0, -1
        case (0, -1):
            return -1, 0
        case _:
            return direction_row, direction_col

position_count = 1
positions_visited = set()
crossing_positions = set()
while (0 <= current_row + direction_row < len(map)) and (0 <= current_col + direction_col < len(map[0])):
    if map[current_row + direction_row][current_col + direction_col] == "#":
        direction_row, direction_col = rotate_90deg_right(direction_row, direction_col)
    else:
        position_count += 1
        if (current_row, current_col) in positions_visited:
            crossing_positions.add((current_row, current_col))
        else:
            positions_visited.add((current_row, current_col))
        current_row += direction_row
        current_col += direction_col
# exit position?
positions_visited.add((current_row, current_col))

print("Total positions visited:", len(positions_visited))
print("Total path crosses:", len(crossing_positions))
print(crossing_positions)