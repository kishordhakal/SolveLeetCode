# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target.You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order.
# Brute Force solution is not that hard for this problem. Pick a number and iterate through the array
# until we get another number which can add up to target together.

# Here we will use different approach, we will try to solve with the time complexity of O(n) and space complexity O(n)
# We will go through the array exactly once, and we keep track of the values that we pass as we iterate though the array
# We will use dictionary to keep track of the numbers we iterate through
from typing import List

from self import self


def twoSum(self, nums:List[int], target: int) -> List[int]:
    prev = {}  # dictionary to keep track of numbers appeared previously
    for x in range(len(nums)):
        diff = target - nums[x]
        if diff in prev:
            return [prev[diff], x]
        prev[nums[x]] = x

#testing
nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6

print("Printing the Result")
print(twoSum(self, nums1, target1))
print(twoSum(self, nums2, target2))
