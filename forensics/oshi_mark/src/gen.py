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


def write_to_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"Data written to {filename} successfully."
    except Exception as e:
        return f"Error writing to file: {e}"


input_text = "well, well, well, look who finally decoded my secret oshi mark message! congratulations on wasting countless hours (and probably brain cells) figuring out that \"awawawa\" means \"i love you!\" maybe you've finally found a use for all that nerdy knowledge you've accumulated over the years. and let's be honest, you couldn't even figure out the message without relying on a secret decoder ring you probably got as a prize in a kids' cereal box. don't worry though, i won't tell anyone! how about this? let's give you a prize for your efforts. how about... jellyCTF{a_cut3_alic3_hugg4bl3_plush13}! awawawawawa! it's cute how nerdy you are."
hex_result = utf8_to_hex(input_text)

final_hex = utf8_to_hex("🌠")
for char in hex_result:
    final_hex += "e2808c"
    final_hex += "efb88"
    final_hex += char
final_hex += utf8_to_hex("🎀")

filename = "../dist/oshimarksothatidonthavetogooglemyownoshimarkwheneversakanawantsmetotweetsomethingAAAIEEEEactuallyletmeaddsomethingformystarknights.txt"
result = write_to_file(filename, hex_to_utf8(final_hex))
print(result)
