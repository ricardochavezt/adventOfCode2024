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
    input_list = []
    for c in code:
        coordinates = button_coordinates(c)
        drow, dcol = coordinates[0]-prev_coordinates[0], coordinates[1]-prev_coordinates[1]
        horiz_input = (">" if dcol > 0 else "<") * abs(dcol)
        vert_input = ("v" if drow > 0 else "^") * abs(drow)
        
        if dcol < 0:
            if (prev_coordinates[0], prev_coordinates[1] + dcol) == gap_coordinates:
                input_list.append(vert_input + horiz_input + "A")
            else:
                input_list.append(horiz_input + vert_input + "A")
        else:
            if (prev_coordinates[0] + drow, prev_coordinates[1]) == gap_coordinates:
                input_list.append(horiz_input + vert_input + "A")
            else:
                input_list.append(vert_input + horiz_input + "A")

        prev_coordinates = coordinates
    
    return "".join(input_list)

if __name__ == "__main__":
    codes = [line.strip() for line in fileinput.input()]

    sum_complexities = 0
    for code in codes:
        input = code
        for n in range(3):
            input = generate_inputs(input)

        print("Complexity:", len(input), "*", int(code[:-1]))
        sum_complexities += (len(input) * int(code[:-1]))

    print("Sum complexities:", sum_complexities)