#!/usr/bin/env python

out = ""
for i in (62, 29, 2, 31, 52, 39, 16, 2, 40):
    out += f"{i:06b}"

print("awa" + out.replace("0", " awa").replace("1", "wa"))
