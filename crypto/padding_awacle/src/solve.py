from pwn import *
import binascii

p = process(['python3', './padding_awacle.py'])

p.recvuntil("Ciphertext in 16 byte blocks:\n")
data = p.recvuntil(b"Enter hex ciphertext to decode: ").decode()
chunks = data.split("\n")[:-1]
print(chunks)

output_string = []
for CHUNK_NUMBER in range(len(chunks)):
    # Decode block-by-block starting from the last chunk
    chunk_to_decode = chunks[-CHUNK_NUMBER]
    previous_ciphertext = chunks[-CHUNK_NUMBER-1]

    print("Chunk number: ", CHUNK_NUMBER)
    print("Decoding chunk:", chunk_to_decode)

    modified_block = [0] * 16

    # In AES CBC, message[n] = cipher[n-1] ^ Decrypt(cipher[n])
    # Lets call Decrypt(cipher[n]) the 'intermediate_block'

    # The awacle will leak information if message [n] ends in AWAWAWA...
    # Modify cipher[n-1] byte by byte and check if the response changes to try and figure out the intermediate_block

    # E.g. for last byte, iterate through all 256 possibilities and find which one replies with 'A'
    # Now we know the last byte of cipher[n-1] that will cause the plaintext to end in 'A' after XOR-ing

    # Set the last byte of cipher[n-1], iterate through 256 possibilities for 2nd last byte and find which gives reply of'WA'
    # Set the 2nd last byte of cipher[n-1], iterate through 256 possibilities for 3rd last byte and find which gives reply of'AWA'
    # etc...


    # Iterate through each byte starting from the last
    for num in range(16):
        # print("Testing byte ", num)
        best_guess = 0

        # Try all possible values per byte
        for i in range(256):
            modified_block[15-num] = i

            hexstring = bytes(modified_block).hex() + chunk_to_decode
            p.sendline(hexstring)
            data = p.recvuntil(b"Enter hex ciphertext to decode: ").decode()
            awacle_response = data.split("\n")[0]

            if num == 0:
                if (awacle_response == 'A'):        # Last byte of oracle phrase
                    # print(i, awacle_response)
                    best_guess = i
            else:
                if len(awacle_response) > num:
                    # print(i, awacle_response)
                    best_guess = i

        modified_block[15-num] = best_guess
        # print(modified_block)

    oracle_phrase = "WAWAWAWAWAWAWAWA"
    prev_chunk_in_int = [int(previous_ciphertext[i:i+2],16) for i in range(0,len(previous_ciphertext),2)]
    # print(prev_chunk_in_int)

    plaintext = [chr(modified_block[n] ^ ord(oracle_phrase[n]) ^ prev_chunk_in_int[n]) for n in range(16)]

    output_string.append(''.join(plaintext))

print(''.join(output_string[::-1]))
p.interactive()