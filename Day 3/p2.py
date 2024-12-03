import os
import re

os.chdir("Day 3")

with open("input.txt") as f:
    lines = f.readlines()

line = "".join(lines)

ops = re.findall(r"mul\(\d+\,\d+\)|do\(\)|don\'t\(\)", line)

enabled = True

total = 0
for x in ops:
    if x == "do()":
        enabled = True
    elif x == "don't()":
        enabled = False
    else:
        if enabled:
            a = int(x[1 + x.index("(") : x.index(",")])
            b = int(x[1 + x.index(",") : x.index(")")])
            total += a * b
print(total)