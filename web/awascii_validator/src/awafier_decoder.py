import awafier_maps
import argparse
import os

DIGITS_PER_AWASCII = 6

# custom debug function
def debug(text):
    os.system('''echo {}'''.format(text))

def awascii_to_binary_string(awascii_text: str):
    buffer = ""
    result = ""

    for char in awascii_text:
        if char == " ":
            buffer = ""
        else:
            buffer += char

        if buffer == "awa":
            result += "0"
            buffer = ""
        elif buffer == "wa":
            result += "1"
            buffer = ""

        if len(buffer) > 3:
            # Something went wrong
            exit("Unexpected - buffer should always be < 3")

    if not len(buffer) == 0:
        exit("Expect buffer to be 0 at end of parsing")

    return result


# Note AWASCII is 6 bits
def awascii_to_text(text: str):
    debug("Decoding AWASCII to sane human text: " + text)

    if len(text) < 3 or not text[0:3] == 'awa':
        debug("Invalid start code - mising starting awa")

    text = text[3:].lstrip()
    binary_string = awascii_to_binary_string(text)

    valid_chars_only = set(text) <= set('aw ')
    repeated_a = 'aa' in text
    repeated_b = 'ww' in text
    multiple_of_AWASCII = len(binary_string) % DIGITS_PER_AWASCII == 0

    if (not valid_chars_only) or repeated_a  or repeated_b or (not multiple_of_AWASCII):
        debug("Input is invalid AWASCII - do better.")
        exit()

    result = ""

    for character in [binary_string[i:i+DIGITS_PER_AWASCII] for i in range(0, len(binary_string), DIGITS_PER_AWASCII)]:
        value = int(character, 2)
        result += awafier_maps.REVERSE_AWASCII_MAP[value]

    debug(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='AwaSCII validator')
    parser.add_argument("input_text")

    args = parser.parse_args()

    awascii_to_text(args.input_text)