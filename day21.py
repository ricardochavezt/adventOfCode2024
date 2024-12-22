import fileinput

def coordinates_num_keypad(button):
    match button:
        case "7":
            return (0,0)
        case "8":
            return (0,1)
        case "9":
            return (0,2)
        case "4":
            return (1,0)
        case "5":
            return (1,1)
        case "6":
            return (1,2)
        case "1":
            return (2,0)
        case "2":
            return (2,1)
        case "3":
            return (2,2)
        case "0":
            return (3,1)
        case "A":
            return (3,2)
        case _:
            return (-1,-1)

def coordinates_dir_keypad(button):
    match button:
        case "^":
            return (0,1)
        case "A":
            return (0,2)
        case "<":
            return (1,0)
        case "v":
            return (1,1)
        case ">":
            return (1,2)
        case _:
            return (-1,-1)
        
def generate_inputs(code):
    if len(code) == 4:
        button_coordinates = coordinates_num_keypad
        gap_coordinates = (3,0)
    else:
        button_coordinates = coordinates_dir_keypad
        gap_coordinates = (0,0)
    
    prev_coordinates = button_coordinates("A")
    input_list = [[]]
    for c in code:
        coordinates = button_coordinates(c)
        drow, dcol = coordinates[0]-prev_coordinates[0], coordinates[1]-prev_coordinates[1]
        horiz_input = (">" if dcol > 0 else "<") * abs(dcol)
        vert_input = ("v" if drow > 0 else "^") * abs(drow)
        if dcol == 0 or drow == 0:
            for l in input_list:
                l.append(horiz_input)
                l.append(vert_input)
                l.append("A")
        else:
            new_input_list = []
            for l in input_list:
                if (prev_coordinates[0], prev_coordinates[1]+dcol) != gap_coordinates:
                    new_input_list.append(l + [horiz_input, vert_input, "A"])
                if (prev_coordinates[0]+drow, prev_coordinates[1]) != gap_coordinates:
                    new_input_list.append(l + [vert_input, horiz_input, "A"])
            input_list = new_input_list
        prev_coordinates = coordinates
    
    return ["".join(l) for l in input_list]

if __name__ == "__main__":
    codes = [line.strip() for line in fileinput.input()]

    sum_complexities = 0
    for code in codes:
        inputs = [code]
        for n in range(3):
            new_inputs = []
            min_len = 2 ** 32
            for input in inputs:
                for new_input in generate_inputs(input):
                    if len(new_input) < min_len:
                        new_inputs = [new_input]
                        min_len = len(new_input)
                    elif len(new_input) == min_len:
                        new_inputs.append(new_input)

            inputs = new_inputs

        print("Complexity:", min_len, "*", int(code[:-1]))
        sum_complexities += (min_len * int(code[:-1]))

        # i1 = sorted(generate_inputs(code), key=len)
        # i2 = []
        # min_len = 2 ** 32
        # for input in i1:
        #     for new_input in generate_inputs(input):
        #         if len(new_input) < min_len:
        #             i2 = [new_input]
        #             min_len = len(new_input)
        #         elif len(new_input) == min_len:
        #             i2.append(new_input)
        # min_len = 2 ** 32
        # for input in i2:
        #     i3 = generate_inputs(input)
        #     current_min_len = min([len(l) for l in i3])
        #     if current_min_len < min_len:
        #         min_len = current_min_len

        # print("Complexity:", min_len, "*", int(code[:-1]))
        # sum_complexities += (min_len * int(code[:-1]))

    print("Sum complexities:", sum_complexities)