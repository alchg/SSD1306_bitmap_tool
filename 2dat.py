import os
import sys

def compress_to_byte(binary_string):
    compressed_byte = 0

    for bit in binary_string:
        compressed_byte = (compressed_byte << 1) | int(bit)

    return compressed_byte

def process_input_file(input_file):
    with open(input_file, 'r') as infile:
        data = infile.read().replace('\n', '')

    compressed_bytes = []
    
    # Reverse the order to make it descending
    for i in range(len(data)-1, -1, -8):
        binary_chunk = data[max(0, i-7):i+1]  # Slice the binary chunk to be 8 bits
        compressed_byte = compress_to_byte(binary_chunk)
        compressed_bytes.append(compressed_byte)

    return bytes(compressed_bytes)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    # Create the "output" folder if it does not exist
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)

    # Remove directory path from input file name
    input_filename = os.path.basename(input_file)
    
    output_filename = os.path.join(output_folder, input_filename[:6] + ".dat")

    compressed_data = process_input_file(input_file)

    with open(output_filename, 'wb') as outfile:
        outfile.write(compressed_data)


