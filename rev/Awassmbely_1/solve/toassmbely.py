import argparse
import re

def bin_to_hex(match):
    binary_str = match.group(0)
    binary_str_padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    hex_num = hex(int(binary_str_padded, 2))[2:]
    return '0x' + hex_num.upper() 

def reverse_print_file_lines(filename):
    binary_pattern = re.compile(r'\b[01]+\b')
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split(':', 1)
            prefix = parts[0] + ':'
            suffix = parts[1]
 
            
            suffix = suffix.replace("aa", "a a")
            suffix = suffix.replace("waw", "wa w")
            suffix = suffix.replace("waw", "wa w")
            suffix = suffix.replace("awa ", "0")
            suffix = suffix.replace("awa", "0")
            suffix = suffix.replace("wa ", "1")
            suffix = suffix.replace("wa", "1")

         
            suffix = binary_pattern.sub(bin_to_hex, suffix)

            print(prefix + suffix, end='')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    
    args = parser.parse_args()
    
    reverse_print_file_lines(args.filename)

if __name__ == "__main__":
    main()
