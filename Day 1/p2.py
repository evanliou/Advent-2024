import os

os.chdir("Day 1")

with open("input.txt") as f:
    lines = f.readlines()

total = 0
nums1 = []
nums2 = {}

for line in lines:
    temp = [int(x) for x in line.split()]
    nums1.append(temp[0])
    nums2[temp[1]] = 1 + nums2.get(temp[1], 0)

for i in nums1:
    total += i * nums2.get(i, 0)
print(total)
