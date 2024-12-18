def execute_program(program, regA=0, regB=0, regC=0, debug=False):

    def get_combo_operand_value(operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand, f"{operand} (literal value)"
            case 4:
                return register_A, "Register A"
            case 5:
                return register_B, "Register B"
            case 6:
                return register_C, "Register C"
            case 7:
                print("Error: reserved value for combo operand:", operand)
                return None, "Error: reserved value for combo operand"
            case _:
                print("Error: invalid value for combo operand:", operand)
                return None, "Error: invalid value for combo operand"

    register_A = regA
    register_B = regB
    register_C = regC
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]

        jump = False
        match opcode:
            case 0:
                operand_value, debug_info = get_combo_operand_value(operand)
                if debug:
                    print(f"register A ({register_A}) div 2^{debug_info} ({operand_value}) -> register A")
                register_A = register_A // (2 ** operand_value)
            case 1:
                if debug:
                    print(f"register B ({register_B}) XOR {operand} -> register B")
                register_B = register_B ^ operand
            case 2:
                operand_value, debug_info = get_combo_operand_value(operand)
                if debug:
                    print(f"{debug_info} ({operand_value}) mod 8 -> register B")
                register_B = operand_value % 8
            case 3:
                if register_A != 0:
                    instruction_pointer = operand
                    jump = True
                    if debug:
                        print(f"Jumping to instruction {operand}")
            case 4:
                if debug:
                    print(f"register B ({register_B}) XOR register C ({register_C}) -> register B")
                register_B = register_B ^ register_C
            case 5:
                operand_value, debug_info = get_combo_operand_value(operand)
                output.append(operand_value % 8)
                if debug:
                    print(f"--- Outputting {debug_info} ({operand_value}) mod 8 ({operand_value % 8})")
            case 6:
                operand_value, debug_info = get_combo_operand_value(operand)
                if debug:
                    print(f"register A ({register_A}) div 2^{debug_info} ({operand_value}) -> register B")
                register_B = register_A // (2 ** operand_value)
            case 7:
                operand_value, debug_info = get_combo_operand_value(operand)
                if debug:
                    print(f"register A ({register_A}) div 2^{debug_info} ({operand_value}) -> register C")
                register_C = register_A // (2 ** operand_value)
            case _:
                print("Error: unrecognized opcode:", opcode)

        if jump:
            jump = False
        else:
            instruction_pointer += 2
    
    print("Register A:", register_A, "- Register B:", register_B, "- Register C:", register_C)
    return output

program = [2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0]

output = execute_program(program, regA=30344604)
print("Program output:", ",".join([str(o) for o in output]))
