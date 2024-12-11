import fileinput
from functools import cache

MAX_LEVEL = 75

@cache
def generate_new_stones(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        return [int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])]
    else:
        return [(stone * 2024)]

stones = []
for line in fileinput.input():
    stones.extend([int(s) for s in line.split()])

count = {s: 1 for s in stones}
for i in range(MAX_LEVEL):
    if i == 25:
        print("Total stones (at 25):", sum(count.values()))

    new_count = {}
    for stone, c in count.items():
        new_stones = generate_new_stones(stone)
        new_count[new_stones[0]] = new_count.get(new_stones[0], 0) + c
        if len(new_stones) > 1:
            new_count[new_stones[1]] = new_count.get(new_stones[1], 0) + c
    count = new_count

print("Total stones:", sum(count.values()))