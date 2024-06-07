flag = "jellyCTF{baba_is_cool_but_j3lly_i5_COOLER}"

with open('list_of_safe_unicode_chars.txt', 'r') as f:
    symbols = f.read()

value = int.from_bytes(flag.encode("utf-8"), byteorder='big', signed=False)
print(value)

base = int("0xBABA", 16)
print(base)

chars = []
while value:
    chars.append(int(value % base))
    value //= base
chars = chars[::-1]
chars = [symbols[x] for x in chars]

print(chars)
result = ''.join(chars)

print(result)
with open ('flag.txt', 'w') as f:
    f.write(result)