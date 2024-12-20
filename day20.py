import fileinput

start, end = None, None
path_set = set()
rows, cols = 0, 0
for i, line in enumerate(fileinput.input()):
    for j, c in enumerate(line.strip()):
        match c:
            case "S":
                start = (i, j)
            case "E":
                end = (i, j)
                path_set.add(end)
            case ".":
                path_set.add((i, j))
    else:
        cols = j + 1
else:
    rows = i + 1

path_list = [start]
pos = start
while pos != end:
    for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
        if (pos[0] + di, pos[1] + dj) in path_set:
            pos = (pos[0] + di, pos[1] + dj)
            path_list.append(pos)
            path_set.remove(pos)
            break
    
print("Path length:", len(path_list))

def count_cheats(max_distance):
    cheat_count_100ps = 0
    for index_start, pos_start in enumerate(path_list):
        for index, pos_end in enumerate(path_list[index_start+1:]):
            index_end = index_start + 1 + index
            distance = abs(pos_start[0]-pos_end[0]) + abs(pos_start[1]-pos_end[1])
            if distance <= max_distance and index_end - index_start - distance >= 100 and distance < index_end - index_start:
                cheat_count_100ps += 1
            
    return cheat_count_100ps

print("# of cheats - part 1:", count_cheats(2))
print("# of cheats - part 2:", count_cheats(20))