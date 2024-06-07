import secrets
import random
from Crypto.Cipher import AES

FLAG = "jellyCTF{je1y_sees_thr0ugh_ev3ryth1ng}"
MESSAGE = f"Man I love Jelly, I hope this flag: {FLAG} isn't too cringe for her?"

BLOCK_SIZE = 16

random.seed(0)
key = random.randbytes(BLOCK_SIZE)
iv = random.randbytes(BLOCK_SIZE)
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

def awapad(text):
    padtext = "AWAWAWAWAWAWAWAWA"
    padlength = BLOCK_SIZE - len(text) % BLOCK_SIZE
    return text + padtext[0:padlength]

def awacle(text):
    # Replies if
    suffix = ""
    prev = ""
    for char in reversed(text):
        if char == ord('A') and prev in ["", "W"]:
            suffix += 'A'
            prev = chr(char)
        elif char == ord('W') and prev in ["", "A"]:
            suffix += 'W'
            prev = chr(char)
        else:
            break
    print(suffix[::-1])

def receive_message(hex_text):
    try:
        decryptor = AES.new(key, AES.MODE_CBC, iv=iv)
        result = decryptor.decrypt(bytes.fromhex(hex_text))
        awacle(result)

    except ValueError as e:
        print(e)

plaintext = awapad(MESSAGE).encode()
ciphertext = cipher.encrypt(plaintext)

print("Ciphertext in hex: ", ciphertext.hex())
print("Ciphertext in 16 byte blocks:")
for i in range(0, len(ciphertext.hex()), 2*BLOCK_SIZE):
    print(ciphertext.hex()[i:i+2*BLOCK_SIZE])

while True:
    x = input("Enter hex ciphertext to decode: ")
    if (x == ""):
        break
    else:
        receive_message(x)
