import fileinput

memory_layout = []

def find_last_file_index(starting_index):
    found_index = starting_index
    while memory_layout[found_index][0] == -1:
        found_index -= 1
    return found_index

file_lengths = []
for line in fileinput.input():
    used_space, free_space = 0, 0
    for index, c in enumerate(line.strip()):
        block_length = int(c)
        if block_length > 0:
            if index % 2 == 0: # file
                memory_layout.append((index // 2, block_length))
                used_space += block_length
                file_lengths.append(block_length)
            else: # free space
                memory_layout.append((-1, block_length))
                free_space += block_length

    index = 0
    index_last_file = find_last_file_index(len(memory_layout) - 1)
    compressed_memory_layout = []
    while index <= index_last_file:
        if memory_layout[index][0] != -1: # file
            compressed_memory_layout.append(memory_layout[index])
        else: # empty space
            available_space = memory_layout[index][1]
            while available_space >= memory_layout[index_last_file][1]:
                compressed_memory_layout.append(memory_layout[index_last_file])
                available_space -= memory_layout[index_last_file][1]
                index_last_file = find_last_file_index(index_last_file-1)
                if index > index_last_file:
                    break
            if available_space > 0 and index <= index_last_file:
                compressed_memory_layout.append((memory_layout[index_last_file][0], available_space))
                memory_layout[index_last_file] = (memory_layout[index_last_file][0], memory_layout[index_last_file][1]-available_space)

        index += 1
    
    break # processing only the first line

compressed_memory_index = 0
total = 0
for file_id, length in compressed_memory_layout:
    file_lengths[file_id] -= length
    file_id_list = [file_id] * length
    positions = range(compressed_memory_index, compressed_memory_index + length)
    checksum = sum([pos * file_id for pos, file_id in zip(positions, file_id_list)])
    total += checksum
    compressed_memory_index += length

print("Total checksum:", total)