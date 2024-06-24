def utf8_to_hex(input_string):
    try:
        ascii_bytes = input_string.encode('utf-8')
        hex_string = ascii_bytes.hex()
        return hex_string
    except Exception as e:
        return f"Error converting to hex: {e}"


def hex_to_utf8(hex_string):
    try:
        byte_data = bytes.fromhex(hex_string)
        utf8_text = byte_data.decode('utf-8')
        return utf8_text
    except ValueError:
        return "Invalid hexadecimal input."
    

def string_to_ascii_array(input_string):
    return [ord(char) for char in input_string]


def write_to_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"Data written to {filename} successfully."
    except Exception as e:
        return f"Error writing to file: {e}"
    
variational_selector = {
    17: "f3a08480",
    18: "f3a08481",
    19: "f3a08482",
    20: "f3a08483",
    21: "f3a08484",
    22: "f3a08485",
    23: "f3a08486",
    24: "f3a08487",
    25: "f3a08488",
    26: "f3a08489",
    27: "f3a0848a",
    28: "f3a0848b",
    29: "f3a0848c",
    30: "f3a0848d",
    31: "f3a0848e",
    32: "f3a0848f",
    33: "f3a08490",
    34: "f3a08491",
    35: "f3a08492",
    36: "f3a08493",
    37: "f3a08494",
    38: "f3a08495",
    39: "f3a08496",
    40: "f3a08497",
    41: "f3a08498",
    42: "f3a08499",
    43: "f3a0849a",
    44: "f3a0849b",
    45: "f3a0849c",
    46: "f3a0849d",
    47: "f3a0849e",
    48: "f3a0849f",
    49: "f3a084a0",
    50: "f3a084a1",
    51: "f3a084a2",
    52: "f3a084a3",
    53: "f3a084a4",
    54: "f3a084a5",
    55: "f3a084a6",
    56: "f3a084a7",
    57: "f3a084a8",
    58: "f3a084a9",
    59: "f3a084aa",
    60: "f3a084ab",
    61: "f3a084ac",
    62: "f3a084ad",
    63: "f3a084ae",
    64: "f3a084af",
    65: "f3a084b0",
    66: "f3a084b1",
    67: "f3a084b2",
    68: "f3a084b3",
    69: "f3a084b4",
    70: "f3a084b5",
    71: "f3a084b6",
    72: "f3a084b7",
    73: "f3a084b8",
    74: "f3a084b9",
    75: "f3a084ba",
    76: "f3a084bb",
    77: "f3a084bc",
    78: "f3a084bd",
    79: "f3a084be",
    80: "f3a084bf",
    81: "f3a08580",
    82: "f3a08581",
    83: "f3a08582",
    84: "f3a08583",
    85: "f3a08584",
    86: "f3a08585",
    87: "f3a08586",
    88: "f3a08587",
    89: "f3a08588",
    90: "f3a08589",
    91: "f3a0858a",
    92: "f3a0858b",
    93: "f3a0858c",
    94: "f3a0858d",
    95: "f3a0858e",
    96: "f3a0858f",
    97: "f3a08590",
    98: "f3a08591",
    99: "f3a08592",
    100: "f3a08593",
    101: "f3a08594",
    102: "f3a08595",
    103: "f3a08596",
    104: "f3a08597",
    105: "f3a08598",
    106: "f3a08599",
    107: "f3a0859a",
    108: "f3a0859b",
    109: "f3a0859c",
    110: "f3a0859d",
    111: "f3a0859e",
    112: "f3a0859f",
    113: "f3a085a0",
    114: "f3a085a1",
    115: "f3a085a2",
    116: "f3a085a3",
    117: "f3a085a4",
    118: "f3a085a5",
    119: "f3a085a6",
    120: "f3a085a7",
    121: "f3a085a8",
    122: "f3a085a9",
    123: "f3a085aa",
    124: "f3a085ab",
    125: "f3a085ac",
    126: "f3a085ad",
    127: "f3a085ae",
    128: "f3a085af"
}

input_text = "well, well, well, look who finally decoded my secret oshi mark message! congratulations on wasting countless hours (and probably brain cells) figuring out that \"awawawa\" means \"i love you!\" maybe you've finally found a use for all that nerdy knowledge you've accumulated over the years. and let's be honest, you probably couldn't even figure out the message without relying on a silly unicode decoding site you found using hints. don't worry though, i won't tell anyone! how about this? let's give you a prize for your efforts. how about... jellyCTF{a_cut3_alic3_hugg4bl3_plush13}! awawawawawawawa! it's cute how nerdy you are."
ascii_result = string_to_ascii_array(input_text)

final_hex = utf8_to_hex("🌠")
for ascii_code in ascii_result:
    final_hex += "e2808c"
    final_hex += variational_selector[ascii_code]
final_hex += utf8_to_hex("🎀")

filename = "../README.md"
result = write_to_file(filename, hex_to_utf8(final_hex))
print(result)

jellyCTF{you_won_cherries!}