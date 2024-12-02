import os

os.chdir("Day 2")

with open("input.txt") as f:
    lines = f.readlines()

safeNum = 0

def allIncreasing(nums):
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True

def allDecreasing(nums):
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            return False
    return True

def adjacentLevels(nums):
    for i in range(len(nums) - 1):
        temp = abs(nums[i] - nums[i + 1])
        if temp < 1 or temp > 3:
            return False
    return True
def valid(nums):
    if (allIncreasing(nums) or allDecreasing(nums)) and adjacentLevels(nums):
        return True
    return False
        
for line in lines:
    nums = [int(x) for x in line.split()]
    possibleNums = [nums[:i] + nums[i+1:] for i in range(len(nums))]
    for arr in possibleNums:
        if valid(arr):
            safeNum += 1
            break


print(safeNum)