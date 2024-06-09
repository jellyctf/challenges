from math import gcd
import sympy

a = sympy.Matrix([[19, 32, 347],
                  [22, 27, 349],
                  [19, 29, 353]])

b1 = sympy.Matrix([10992,30978,12520])
b2 = sympy.Matrix([30983,7390,481])
b3 = sympy.Matrix([25974,26744,9122])
m = 32768

def solve(b):
    det = int(a.det())
    if gcd(det, m) == 1:
        ans = ((pow(det, -1, m) * a.adjugate()) @ b) % m
        return ans
    else:
        print("don't know")

def decToAwascii32(x):
    awascii32 = r'awjelyhosiumpcntbdfgr.,!{}_/;CTF'
    return awascii32[x % 32] + awascii32[(x >> 5) % 32] + awascii32[(x >> 10) % 32]

x1,x2,x3 = solve(b1)
print(f'{decToAwascii32(m-x1)}{decToAwascii32(m-x2)}{decToAwascii32(m-x3)}')
x1,x2,x3 = solve(b2)
print(f'{decToAwascii32(m-x1)}{decToAwascii32(m-x2)}{decToAwascii32(m-x3)}')
x1,x2,x3 = solve(b3)
print(f'{decToAwascii32(m-x1)}{decToAwascii32(m-x2)}{decToAwascii32(m-x3)}')