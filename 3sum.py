# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.  Notice that the solution set must not contain duplicate triplets.

# Here  we are trying to find all triplets so that sum of them is 0.
# Here one strategy will be to Pick a number and use two sum trick to find the other numbers.
# first we sort the array.

from typing import List
from self import self

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
              r -= 1
            elif sum < 0:
              l += 1
            else:
                res.append([nums[l], nums[r], a])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

# testing
n = [-1, 0, 1, 2, -1, -4]
print("List: ", n)
print(threeSum(self, n))

n2 = [0,1,1]
print("List: ", n2)
print(threeSum(self, n2))

n3 = [0,0,0]
print("List: ", n3)
print(threeSum(self, n3))

