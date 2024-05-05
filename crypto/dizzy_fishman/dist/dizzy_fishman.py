import time
from Crypto.Util import number
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

P_LENGTH = 256
MAX_INT = 10000

p = number.getPrime(P_LENGTH)
secret_A = number.getRandomRange(2, MAX_INT)
secret_B = number.getRandomRange(2, MAX_INT)

print("Intercepting communications...")
time.sleep(1)

print("Randomly selected prime p = ", p)
g = int(input("Inject a generator g: "))

if not (1 < g < p):
    print("ALERT: Invalid g detected, requires 1 < g < p. Communications terminated!")
    exit()

public_key_A = pow(g, secret_A, p)
print("Dizzy's public key (integer) : ", public_key_A)

public_key_B = pow(g, secret_B, p)
print("Sakana's public key (integer): ", public_key_B)

print("Dizzy and Sakana are calculating their secret keys...", end='\n')
secret_dizzy = pow(public_key_B, secret_A, p)
secret_sakana = pow(public_key_A, secret_B, p)
# The secret key should be the same for both parties
assert(secret_dizzy == secret_sakana)

print("Encrypting flag with AES-256 using shared secret key")
with open('flag.txt', 'r') as f:
    flag = f.read().strip("\n").encode()

secret = secret_dizzy
encoded_key = secret.to_bytes(32, byteorder='big')
cipher = AES.new(encoded_key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(flag, 32))
print("Encrypted flag received: ", ciphertext.hex())