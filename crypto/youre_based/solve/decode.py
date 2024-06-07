base = int("0xBABA", 16)

with open('flag.txt', 'r') as f:
    encoded = f.read()

with open('list_of_safe_unicode_chars.txt', 'r') as f:
    symbols = f.read()

print(encoded)

numeric = [symbols.find(x) for x in encoded]
print(numeric)

resulting_number = 0
for x in numeric:
    resulting_number *= base
    resulting_number += x

#[2:] to get rid of the '0x' at the start of hex string
print(bytes.fromhex(hex(resulting_number)[2:]).decode())