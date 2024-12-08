import fileinput
import re

antennas_by_frequency = {}
antenna_re = re.compile(r"[^.]")
map_row_count = 0
map_col_count = 0

for index, line in enumerate(fileinput.input()):
    for match in antenna_re.finditer(line.strip()):
        antennas_by_frequency.setdefault(match[0], []).append((index, match.start()))

    map_row_count, map_col_count = index, len(line.strip())

map_row_range = range(map_row_count+1)
map_col_range = range(map_col_count)
antinodes = set()
first_antinodes = set()
for (frequency, locations) in antennas_by_frequency.items():
    if len(locations) > 2:
        for i, a1 in enumerate(locations):
            for a2 in locations[i+1:]:
                diff = (a2[0]-a1[0], a2[1]-a1[1])
                possible_location = a2
                first_antinode = True
                while possible_location[0] in map_row_range and possible_location[1] in map_col_range:
                    antinodes.add(possible_location)
                    if first_antinode and possible_location != a2:
                        first_antinodes.add(possible_location)
                        first_antinode = False
                    possible_location = (possible_location[0] + diff[0], possible_location[1] + diff[1])
                possible_location = a1
                first_antinode = True
                while possible_location[0] in map_row_range and possible_location[1] in map_col_range:
                    antinodes.add(possible_location)
                    if first_antinode and possible_location != a1:
                        first_antinodes.add(possible_location)
                        first_antinode = False
                    possible_location = (possible_location[0] - diff[0], possible_location[1] - diff[1])

print("First antinodes:", len(first_antinodes))
print("Total antinodes:", len(antinodes))