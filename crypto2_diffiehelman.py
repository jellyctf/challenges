import base64
from Crypto.Util import number
from Crypto.Cipher import AES

P_LENGTH = 256
MAX_INT = 10000

p = number.getPrime(P_LENGTH)
secret_A = number.getRandomRange(2, MAX_INT)
secret_B = number.getRandomRange(2, MAX_INT)

print("Selected prime p = ", p)

# Try to find an input that let's you identify the shared key
g = int(input("Enter a public g: "))

if not (1 < g < p):
    print("Invalid g! Requires 1 < g < p")
    exit()

print("A calculates the public key A = g^(private key A) mod p and sends to B")
public_key_A = pow(g, secret_A, p)
print("Public key A: ", public_key_A)

print("B calculates the public key B = g^(private key B) mod p and sends to A")
public_key_B = pow(g, secret_B, p)
print("Public key B: ", public_key_B)

print("A and B calculate shared secret keys s = (public key B ^ private key A) mod p = (public key A ^ private key B) mod p")
secret = pow(public_key_B, secret_A, p)

# Verify the secret keys
assert (secret == pow(public_key_A, secret_B, p))
# print(secret)                         # Debugging

# Use secret key to encrypt AES
flag = "jellyCTF{crypto_diffie_hellman9}".encode()

print("Encrypt flag with AES-256")
encoded_key = secret.to_bytes(32, byteorder='big')
cipher = AES.new(encoded_key, AES.MODE_ECB)
ciphertext = cipher.encrypt(flag)
print("Hex: ", ciphertext.hex())
#print("Hex: ", encoded_key.hex())      # Debugging
