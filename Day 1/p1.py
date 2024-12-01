import os

os.chdir("Day 1")

with open("input.txt") as f:
    lines = f.readlines()

total = 0
nums1 = []
nums2 = []

for line in lines:
    temp = [int(x) for x in line.split()]
    nums1.append(temp[0])
    nums2.append(temp[1])

nums1.sort()
nums2.sort()

for i in range(len(nums1)):
    total += abs(nums1[i] - nums2[i])
print(total)
