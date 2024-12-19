import fileinput

designs = []
available_patterns = []

if __name__ == "__main__":
    for index, line in enumerate(fileinput.input()):
        if index == 0:
            available_patterns = [p.strip() for p in line.split(",")]
        elif len(design := line.strip()) > 0:
            designs.append(design)

cache = {}

def look_for_design(design, patterns):
    if len(design) == 0:
        return 1

    if design in cache:
        return cache[design]

    sum_patterns = 0
    for pattern in patterns:
        if len(pattern) <= len(design) and design.startswith(pattern):
            sum_patterns += look_for_design(design[len(pattern):], patterns)

    cache[design] = sum_patterns
    return sum_patterns

possible_designs = 0
every_possible_design = 0
for design in designs:
    if (possible_combinations := look_for_design(design, available_patterns)):
        possible_designs += 1
        every_possible_design += possible_combinations
    else:
        pass

print("Total possible designs:", possible_designs)
print("Total - every possible design:", every_possible_design)