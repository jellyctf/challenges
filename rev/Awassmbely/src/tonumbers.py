import argparse
import re

def hex_to_bin(match):
    hex_num = match.group(0)
    bin_num = bin(int(hex_num, 16))[2:] 
    return bin_num

def print_file_lines(filename):
    hex_pattern = re.compile(r'\b0x[0-9A-Fa-f]+\b')
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split(':', 1)
            prefix = parts[0] + ':'  
            suffix = parts[1]  
            modified_suffix = hex_pattern.sub(hex_to_bin, suffix)
            modified_suffix = modified_suffix.replace("0", "awa")
            modified_suffix = modified_suffix.replace("1", "wa")
            print(prefix + modified_suffix, end='')

            
   

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    
    args = parser.parse_args()
    
    print_file_lines(args.filename)

if __name__ == "__main__":
    main()
