import fileinput
from functools import reduce

corrupted_locations_sequence = []
for index, line in enumerate(fileinput.input()):
    str_x, str_y = line.strip().split(",")
    corrupted_locations_sequence.append((int(str_x), int(str_y)))

MAX_X = 70
MAX_Y = 70

def find_path(start, goal, corrupted_locations):
    def h(n):
        return abs(n[0] - goal[0]) + abs(n[1] - goal[1])

    def reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)

        return path

    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h(start)}

    while len(open_set) > 0:
        current = reduce(lambda n1, n2: n1 if f_score.get(n1, MAX_X*MAX_Y) < f_score.get(n2, MAX_X*MAX_Y) else n2, open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if neighbor[0] in range(MAX_X+1) and neighbor[1] in range(MAX_Y+1) and neighbor not in corrupted_locations:
                tentative_g_score = g_score.get(current, MAX_X*MAX_Y) + 1
                if tentative_g_score < g_score.get(neighbor, MAX_X*MAX_Y):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + h(neighbor)
                    if neighbor not in open_set:
                        open_set.add(neighbor)
    
    return None

path = find_path((0,0), (MAX_X, MAX_Y), set(corrupted_locations_sequence[:1024]))
if path:
    print("Number of steps:", len(path)-1)
else:
    print("no path found :(")

# part 2 - brute force FTW
for i in range(1024, len(corrupted_locations_sequence)):
    if not find_path((0,0), (MAX_X, MAX_Y), set(corrupted_locations_sequence[:i+1])):
        print("First byte to cut off:", corrupted_locations_sequence[i])
        break