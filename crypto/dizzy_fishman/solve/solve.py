from pwn import process
from Crypto.Cipher import AES

r = process(["python3", "dizzy_fishman.py"])

r.recvuntil(b"prime p = ")
p = int(r.recvline().decode().strip("\n"))
print("p : ", p)
r.recvuntil(b"generator g: ")

g = p-1
print("g : ", g)
r.sendline(str(g).encode())

r.recvuntil(b"Encrypted flag received:  ")
ciphertext = r.recvline().decode().strip("\n")
print("Ciphertext: ", ciphertext)

# With g = p-1, the secret key can be either 1 or p-1
print("Trying ", g, " as secret key")
try:
    encoded_key = g.to_bytes(32, byteorder='big')
    cipher = AES.new(encoded_key, AES.MODE_ECB)
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext)).decode()
    print(plaintext)
except:
    pass

print("Trying ", 1, " as secret key")
try:
    encoded_key = (1).to_bytes(32, byteorder='big')
    cipher = AES.new(encoded_key, AES.MODE_ECB)
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext)).decode()
    print(plaintext)
except:
    pass