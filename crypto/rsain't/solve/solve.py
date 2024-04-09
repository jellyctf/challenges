import math

# code for generating values
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# these were chose - n explicitly not prime
n = 37373737373737373737373737373737373737373737373737373737
e = 65537

# Key step is finding carmichale/totient function (Wolfram Alpha)
l = 118299807049506757013716473231626400

print("d, e, l")
assert math.gcd(e, l) == 1
d = modinv(e, l)             # d = 101389777715851275381897868150010273
print(d, e, d * e % l)
assert (d * e) % l == 1

flag = "jellyCTF{a_bit_quirky}"
m = int.from_bytes(flag.encode(), 'big')

print("m: ", m)
print("m hex: ", hex(m))

c = pow(m, e, n)
print("c: ", c)
print("c hex: ", hex(c))

result = pow(c, d, n)
print("Result: ", hex(result))
assert result == m