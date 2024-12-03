import os
import re

os.chdir("Day 3")

with open("input.txt") as f:
    lines = f.readlines()

line = "".join(lines)

multOps = re.findall(r"mul\(\d+\,\d+\)", line)

total = 0

for x in multOps:
    a = int(x[1 + x.index("(") : x.index(",")])
    b = int(x[1 + x.index(",") : x.index(")")])
    total += a * b
print(total)