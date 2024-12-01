import fileinput

list_left = []
list_right = []
for line in fileinput.input():
    numbers = line.strip().split()
    list_left.append(int(numbers[0]))
    list_right.append(int(numbers[1]))

list_left.sort()
list_right.sort()

total_distance = 0
for n1, n2 in zip(list_left, list_right):
    total_distance += abs(n1 - n2)

print("Total distance:", total_distance)

similarity_score = 0

second_index = 0
last_count = 0
for index, n in enumerate(list_left):
    if index == 0 or list_left[index-1] != n: # we count the first time, and each time the number changes
        last_count = 0
        while second_index < len(list_right) and list_right[second_index] <= n:
            if list_right[second_index] == n:
                last_count += 1
            second_index += 1

    similarity_score += (last_count * n)

print("Similarity score:", similarity_score)