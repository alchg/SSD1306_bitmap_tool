import os
import sys

def reverse_lines(input_file_path, output_folder):
    # Create the folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # Generate output file name from the input file name
    input_file_name = os.path.basename(input_file_path)
    output_file_name = input_file_name[:6] + '.rvh'
    output_file_path = os.path.join(output_folder, output_file_name)

    # Read the file
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Reverse each line from left to right
    flipped_lines = [''.join(reversed(line.strip())) for line in lines]

    # Write the reversed lines to a new file
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(flipped_lines))

if __name__ == "__main__":
    # Get the input file path from the command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_folder = 'rvh'

    # Execute the reverse process
    reverse_lines(input_file_path, output_folder)

