def extract_every_12th_hex_character(filename):
    try:
        with open(filename,'rb') as f:
            # Read the file as a hex string
            out_hex = f.read().hex()
            # Trim the emojis at the beginning and end of the file
            trimmed_hex = out_hex[8:-8]
            # Extract every 12th hex character
            hex_characters = [trimmed_hex[i] for i in range(11, len(trimmed_hex), 12)]
            return ''.join(hex_characters)
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"Error reading file: {e}"
    
def decode_hex(hex):
    return bytes.fromhex(hex).decode('utf-8')

# Example usage
filename = "../dist/oshimarksothatidonthavetogooglemyownoshimarkwheneversakanawantsmetotweetsomethingiswearimgonnahexhimintoasheepAAAIEEEEactuallyletmeaddsomethingformystarknights.txt"
result = extract_every_12th_hex_character(filename)
print(f"Hex Code: {result}")
print(f"Secret Message: {decode_hex(result)}")