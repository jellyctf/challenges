#!/usr/bin/env python

from pwn import *

p = process("./the_brewing_secrets")

n = 5
g = cyclic_gen("01", n=n)
seq = g.get()
info([seq[i:i+n] for i in range(0, len(seq), n)])

for phase in range(10):
    for i in range(len(seq)//n):
        info(seq)
        try:
            out = p.sendlineafter((b"Enter 5-digit binary passcode", b"Passcode incorrect. Try again!"), seq)
        except EOFError:
            info(b"EOF " + out)
        info(out)
        if b"Phase" in out:
            break
p.interactive()
