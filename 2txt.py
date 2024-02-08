import struct
import sys
import os

def read_bmp_header(file_path):
    with open(file_path, 'rb') as file:
        file.seek(10)
        data_offset = struct.unpack('<I', file.read(4))[0]
        file.seek(18)
        width = struct.unpack('<I', file.read(4))[0]
        height = struct.unpack('<I', file.read(4))[0]
        file.seek(28)
        bit_count = struct.unpack('<H', file.read(2))[0]
        file.seek(34)
        image_size = struct.unpack('<I', file.read(4))[0]

    return data_offset, width, height, bit_count, image_size

def read_pixel_data(file, bit_count):
    if bit_count == 24:
        pixel_data = file.read(3)
    elif bit_count == 32:
        pixel_data = file.read(4)
    else:
        raise ValueError("Unsupported bit count: {}".format(bit_count))

    return pixel_data

def save_image_data_to_file(file_path, bit_count, output_folder):
    data_offset, width, height, _, _ = read_bmp_header(file_path)

    output_file_name = os.path.join(output_folder, os.path.basename(file_path)[:6] + ".txt")

    with open(file_path, 'rb') as file:
        file.seek(data_offset)

        image_data = []

        for _ in range(height):
            row_data = []
            for _ in range(width):
                pixel_data = read_pixel_data(file, bit_count)
                if pixel_data == b'\x00\x00\x00':
                    row_data.append("0")
                elif pixel_data == b'\xFF\xFF\xFF':
                    row_data.append("1")
                else:
                    row_data.append("?")
            image_data.append(row_data)

        with open(output_file_name, 'w') as output_file:
            for row in image_data:
                output_file.write("".join(row) + "\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <BMP_FILE_PATH>")
        sys.exit(1)

    bmp_file_path = sys.argv[1]
    _, width, height, bit_count, _ = read_bmp_header(bmp_file_path)

    output_folder = "txt"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    save_image_data_to_file(bmp_file_path, bit_count, output_folder)

if __name__ == "__main__":
    main()

