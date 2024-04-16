from collections import defaultdict
import random

with open('luminary.txt', 'r') as f:
    data = f.read().split("\n")

letter_dict = defaultdict(list)

for i, row in enumerate(data):
    for j, letter in enumerate(row):
        str_val = "{}.{}".format(i+1, j+1)

        letter_dict[letter].append(str_val)

# print(letter_dict)

plaintext = "Capitalise 'megalencephaly' for the next password"

result = ""
for letter in plaintext:
    if letter == ' ':
        result = result + "\n"
        continue
    datadict = letter_dict[letter]

    if (len(datadict) == 0):
        print("ERROR")
        exit()

    codeword = datadict.pop(random.randrange(len(datadict)))
    result += codeword + " "

print(result)

with open('cipher_luminary.txt', 'w') as f:
    f.write(result)

