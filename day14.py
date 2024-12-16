import sys
import re
from functools import reduce

robot_re = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
WIDTH = 101
HEIGHT = 103
N_SECONDS = 100

occupied_tiles = {}
robots = []
for line in sys.stdin:
    if (match := robot_re.match(line.strip())):
        position_x, position_y = int(match[1]), int(match[2])
        velocity_x, velocity_y = int(match[3]), int(match[4])
        robots.append((position_x, position_y, velocity_x, velocity_y))
        new_position = (position_x + velocity_x * N_SECONDS) % WIDTH, (position_y + velocity_y * N_SECONDS) % HEIGHT
        occupied_tiles[new_position] = occupied_tiles.get(new_position, 0) + 1

quadrant_counts = [0] * 4
for position, count in occupied_tiles.items():
    if position[0] < WIDTH // 2:
        if position[1] < HEIGHT // 2:
            quadrant_counts[0] += count
        elif position[1] > HEIGHT // 2:
            quadrant_counts[1] += count
    elif position[0] > WIDTH // 2:
        if position[1] < HEIGHT // 2:
            quadrant_counts[2] += count
        elif position[1] > HEIGHT // 2:
            quadrant_counts[3] += count

safety_factor = reduce(lambda x, y: x * y, quadrant_counts)
print("Safety factor (after", N_SECONDS, "seconds):", safety_factor)

part2 = len(sys.argv) > 1 and sys.argv[1] == "--part2"
if part2:
    def build_robot_positions_display():
        map_display = ["." * WIDTH] * HEIGHT
        for position, _ in occupied_tiles.items():
            map_display[position[1]] = map_display[position[1]][:position[0]] + "X" + map_display[position[1]][position[0]+1:]

        return map_display

    max_occupied_x = 0
    repeated_x = re.compile("X+")
    for n in range(10000):
        occupied_tiles = {}
        for position_x, position_y, velocity_x, velocity_y in robots:
            new_position = (position_x + velocity_x * n) % WIDTH, (position_y + velocity_y * n) % HEIGHT
            occupied_tiles[new_position] = occupied_tiles.get(new_position, 0) + 1

        map_display = build_robot_positions_display()
        for line in map_display:
            for match in repeated_x.findall(line):
                if len(match) > max_occupied_x and n > 0:
                    max_occupied_x = len(match)
                    print("Iteration", n)
                    print("\n".join(map_display))
