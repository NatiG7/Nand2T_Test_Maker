import itertools
import subprocess

def myInit():
    # Welcome message and instructions
    print("Welcome to the Logic Gate and Circuit Tester Program!")
    print("This program will help you generate test and comparison files for various logic gates and circuits.")
    print("You will be prompted to enter module details including the type of gate, number of inputs and outputs, and their names.")
    print("Let's get started!\n")

def install_dependencies():
    # Making sure users have the required libraries.
    try:
        import colorama
    except ImportError:
        print("Installing colorama...")
        subprocess.check_call(["pip", "install", "colorama"])

    try:
        import tqdm
    except ImportError:
        print("Installing tqdm...")
        subprocess.check_call(["pip", "install", "tqdm"])


from tqdm import tqdm
from colorama import init,Fore
def get_input_info():
    # Function to get user input for the module name, the type of gate or chip,
    # the number and names of inputs and outputs.

    # Returns:
    #     tuple: Contains the module name, type of gate, number of inputs, input names,
    #             number of outputs, and output names.

    # Define valid gate types
    valid_gate_types = [
        "AND", "OR", "NAND", "NOR", "XOR", "XNOR", "NOT",
        "MUX", "DEMUX",
        "HALF_ADDER", "FULL_ADDER", "4_BIT_ADDER",
        "2_TO_4_DECODER", "3_TO_8_DECODER",
        "PRIORITY_ENCODER",
        "OR16", "AND16", "NOT16",
        "CUSTOM"
    ]

    # Module name input validation
    while True:
        module_name = input("Enter the name of the module: ").strip()
        if module_name:
            break
        else:
            print(Fore.RED +"Module name cannot be empty." + Fore.RESET)

    # Gate type input validation
    while True:
        gate_type = input(
            "Enter the type of gate or chip:\n"
            "  - Basic Gates: AND, OR, NAND, NOR, XOR, XNOR, NOT\n"
            "  - Compound Gates: MUX, DEMUX\n"
            "  - Adders: HALF_ADDER, FULL_ADDER, 4_BIT_ADDER\n"
            "  - Decoders: 2_TO_4_DECODER, 3_TO_8_DECODER\n"
            "  - Encoders: PRIORITY_ENCODER\n"
            "  - Multi-Bit Gates: OR16, AND16, NOT16\n"
            "  - Custom Logic: CUSTOM\n"
            "> "
        ).strip().upper()
        if gate_type in valid_gate_types:
            break
        else:
            print(Fore.RED + "Invalid gate type. Please enter a valid gate type." + Fore.RESET)

    # Number of inputs input validation
    while True:
        try:
            num_inputs = int(input("Enter the number of inputs: "))
            if num_inputs > 0:
                break
            else:
                print("Number of inputs must be a positive integer.")
        except ValueError:
            print("Please enter a valid integer for the number of inputs.")

    # Input names input validation
    input_names = []
    print("Enter input names:")
    print()
    for i in tqdm(range(num_inputs),ncols=80):
        while True:
            input_name = input(Fore.CYAN + f"\n### Enter name for input {i+1}: " + Fore.RESET).strip()
            if input_name:
                input_names.append(input_name)
                break
            else:
                print("Input name cannot be empty.")

    # Number of outputs input validation
    while True:
        try:
            num_outputs = int(input("Enter the number of outputs: "))
            if num_outputs > 0:
                break
            else:
                print("Number of outputs must be a positive integer.")
        except ValueError:
            print("Please enter a valid integer for the number of outputs.")

    # Output names input validation
    output_names = []
    print("Enter output names:")
    for i in tqdm(range(num_outputs), ncols=80):
        while True:
            output_name = input(f"\n### Enter name for output {i+1}: ").strip()
            if output_name:
                output_names.append(output_name)
                break
            else:
                print("Output name cannot be empty.")

    return module_name, gate_type, num_inputs, input_names, num_outputs, output_names


def format_output_list(names, gate_type):
    # Formats the output list with specific spacing and format for a .tst file.

    # Args:
    #     names (list): List of input/output names.
    #     gate_type (str): Type of the gate or chip.

    # Returns:
    #     str: Formatted output list string.

    if gate_type in ["AND16", "OR16", "NOT16"]:
        return " ".join([f"{name}%B16.1.16" for name in names])
    else:
        return " ".join([f"{name}%B3.1.3" for name in names])


def generate_test_file(module_name, num_inputs, input_names, output_names, bit_width, gate_type):

    # Function to generate the .tst file for testing the specified module.

    # Args:
    #     module_name (str): The name of the module.
    #     num_inputs (int): Number of input pins.
    #     input_names (list): List of input pin names.
    #     output_names (list): List of output pin names.
    #     bit_width (int): Bit width for display.
    #     gate_type (str): Type of the logical gate or chip.

    with open(f"{module_name}.tst", "w") as f:
        f.write(f"// This file tests the {module_name} module\n")
        f.write(f"load {module_name}.hdl,\n")
        f.write(f"output-file {module_name}.out,\n")
        f.write(f"compare-to {module_name}.cmp,\n")
        f.write("output-list " + format_output_list(input_names + output_names, gate_type) + ";\n\n")

        if gate_type in ["AND16", "OR16", "NOT16"]:
            sample_inputs = [
                ('0000000000000000', '0000000000000000'),
                ('0000000000000000', '1111111111111111'),
                ('1111111111111111', '1111111111111111'),
                ('1010101010101010', '0101010101010101'),
                ('0011110011000011', '0000111111110000'),
                ('0001001000110100', '1001100001110110')
            ]

            if gate_type == "NOT16":
                sample_inputs = [(pair[0],) for pair in sample_inputs]

            for inputs in sample_inputs:
                for name, value in zip(input_names, inputs):
                    f.write(f"set {name} %B{value},\n")
                f.write("eval,\n")
                f.write("output;\n\n")
        else:
            for inputs in itertools.product('01', repeat=num_inputs):
                binary_inputs = "".join(inputs)
                f.write(f"// Test {binary_inputs}\n")
                for name, value in zip(input_names, inputs):
                    f.write(f"set {name} {value},\n")
                f.write("eval,\n")
                f.write("output;\n\n")


def generate_cmp_file(module_name, gate_type, num_inputs, input_names, num_outputs, output_names):

    # Function to generate the .cmp file based on specified logic.

    # Args:
    #     module_name (str): The name of the module.
    #     gate_type (str): Type of the logical gate or chip.
    #     num_inputs (int): Number of input pins.
    #     input_names (list): List of input pin names.
    #     num_outputs (int): Number of output pins.
    #     output_names (list): List of output pin names.

    # Calculate the bit width based on the formatting needs
    bit_width = 16 if gate_type in ["AND16", "OR16", "NOT16"] else 1

    # Create headers for the file with appropriate spacing
    header = "|" + "|".join([f" {name:^{bit_width * 2 + 3}} " for name in input_names + output_names]) + "|"

    with open(f"{module_name}.cmp", "w") as cmp_file:
        cmp_file.write(header + "\n")

        # Generate all possible input combinations
        for inputs in itertools.product('01', repeat=num_inputs):
            output_values = calculate_outputs(gate_type, inputs)
            formatted_line = format_cmp_output_line(inputs, output_values, gate_type, num_inputs)
            cmp_file.write(formatted_line + "\n")

from functools import reduce

def calculate_outputs(gate_type, inputs):

    # Function to calculate the outputs based on the gate type and inputs.
    
    # Args:
    #     gate_type (str): Type of the logical gate or chip.
    #     inputs (tuple): Tuple containing input values as strings.
    
    # Returns:
    #     list: List containing output values as strings.

    # Convert input strings to integers for bitwise operations
    inputs = list(map(int, inputs))
    
    if gate_type == "AND":
        # AND gate output: 1 if all inputs are 1, else 0
        return [str(int(all(inputs)))]
    elif gate_type == "OR":
        # OR gate output: 1 if any input is 1, else 0
        return [str(int(any(inputs)))]
    elif gate_type == "NAND":
        # NAND gate output: 0 if all inputs are 1, else 1
        return [str(int(not all(inputs)))]
    elif gate_type == "NOR":
        # NOR gate output: 0 if any input is 1, else 1
        return [str(int(not any(inputs)))]
    elif gate_type == "XOR":
        # XOR gate output: 1 if an odd number of inputs are 1, else 0
        result = inputs[0]
        for i in inputs[1:]:
            result ^= i
        return [str(result)]
    elif gate_type == "NOT":
        # NOT gate output: inverts the input (1 -> 0, 0 -> 1)
        return [str(1 - inputs[0])]
    elif gate_type in ["AND16", "OR16", "NOT16"]:
        # Handle 16-bit wide gates
        a = int(inputs[0], 2)
        if gate_type != "NOT16":
            b = int(inputs[1], 2)
        if gate_type == "AND16":
            return [format(a & b, '016b')]
        elif gate_type == "OR16":
            return [format(a | b, '016b')]
        elif gate_type == "NOT16":
            return [format(~a & 0xFFFF, '016b')]
    elif gate_type == "XNOR":
    # XNOR gate output: 1 if an even number of inputs are 1, else 0
        result = inputs[0]
        for i in inputs[1:]:
            result ^= i
        return [str(int(not result))]
    elif gate_type == "MUX":
        # MUX output: select input based on selector
        selector = inputs[-1]
        return [str(inputs[selector])]
    elif gate_type == "DEMUX":
        # DEMUX output: route input to one of the outputs based on selector
        selector = inputs[-1]
        outputs = ['0'] * (2 ** (len(inputs) - 1))
        outputs[selector] = str(inputs[0])
        return outputs
    elif gate_type == "HALF_ADDER":
        # HALF_ADDER: sum and carry out
        a, b = inputs
        sum_result = a ^ b
        carry_out = a & b
        return [str(sum_result), str(carry_out)]
    elif gate_type == "FULL_ADDER":
        # FULL_ADDER: sum and carry out with carry in
        a, b, carry_in = inputs
        sum_result = a ^ b ^ carry_in
        carry_out = (a & b) | (b & carry_in) | (carry_in & a)
        return [str(sum_result), str(carry_out)]
    elif gate_type == "4_BIT_ADDER":
        # 4_BIT_ADDER: add two 4-bit numbers
        a = int("".join(map(str, inputs[:4])), 2)
        b = int("".join(map(str, inputs[4:8])), 2)
        result = a + b
        return [format(result, '04b')]
    elif gate_type == "2_TO_4_DECODER":
        # 2_TO_4_DECODER: decode 2-bit input to 4-bit output
        selector = int("".join(map(str, inputs)), 2)
        outputs = ['0'] * 4
        outputs[selector] = '1'
        return outputs
    elif gate_type == "3_TO_8_DECODER":
        # 3_TO_8_DECODER: decode 3-bit input to 8-bit output
        selector = int("".join(map(str, inputs)), 2)
        outputs = ['0'] * 8
        outputs[selector] = '1'
        return outputs
    elif gate_type == "PRIORITY_ENCODER":
        # PRIORITY_ENCODER: encode highest priority input
        for i, input_val in enumerate(reversed(inputs)):
            if input_val == 1:
                return [format(len(inputs) - 1 - i, '03b')]
        return ['0' * len(inputs)]
    
    elif gate_type == "CUSTOM":
        # Example custom logic: simple adder with sum and carry out
        if len(inputs) == 2:
            sum_result = (inputs[0] + inputs[1]) % 2
            carry_out = (inputs[0] & inputs[1])
            return [str(sum_result)]  # Only return sum_result as a single output bit
        else:
            return [str(sum(inputs) % 2)]


def format_cmp_output_line(inputs, output_values, gate_type, num_inputs):

    # Function to format a single line in the .cmp file.

    # Args:
    #     inputs (tuple): Tuple containing input values.
    #     output_values (list): List containing output values.
    #     gate_type (str): Type of the logical gate or chip.
    #     num_inputs (int): Number of input pins.
    # Returns:
    #     str: Formatted line for the .cmp file.

    # Calculate spacing based on the maximum bit width (assuming 1-bit or 16-bit values)
    max_bit_width = 16 if gate_type in ["AND16", "OR16", "NOT16"] else 1

    # Format the input values with proper spacing
    inputs_str = " | ".join([f" {value:^{max_bit_width * 1 + 2}} " for value in inputs])
    
    # Format the output values with proper spacing
    outputs_str = "".join([f" {value:^{max_bit_width * 2 + 1}} " for value in output_values])

    # Combine input and output values into a single line
    formatted_line = f"| {inputs_str} | {outputs_str} |"

    return formatted_line


def main():
    # Main function that orchestrates the generation of test and comparison files.
    
    # Welcome message and instructions
    myInit()
    # Check dependencies and install if necessary
    install_dependencies()
    # Get input and output information from the user
    module_name, gate_type, num_inputs, input_names, num_outputs, output_names = get_input_info()
    
    # Determine the bit width for the truth table display
    bit_width = 16 if gate_type in ["AND16", "OR16", "NOT16"] else 1
    
    # Generate the test file
    generate_test_file(module_name, num_inputs, input_names, output_names, bit_width, gate_type)
    
    # Generate the comparison file
    generate_cmp_file(module_name, gate_type, num_inputs, input_names, num_outputs, output_names)
    
    # Print a message indicating successful file generation
    print(Fore.GREEN + f"Test file ({module_name}.tst) and comparison file ({module_name}.cmp) generated." + Fore.RESET)

if __name__ == "__main__":
    main()

