# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.  Notice that the solution set must not contain duplicate triplets.

# Here  we are trying to find all triplets so that sum of them is 0.
# Here one strategy will be to Pick a number and use two sum trick to find the other numbers.
# first we sort the array and enumerate it.


from typing import List
from self import self


def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:  # here we check if two consecutive element are same then we skip
            continue
        l, r = i + 1, len(nums) - 1  # left and right pointer
        while l < r:
            sum = a + nums[l] + nums[r]  # we calculate sum
            if sum > 0:
                r -= 1  # since our array is sorted and if sum is greater than 0 we need to decrease the right pointer
            elif sum < 0: # if the sum is less than zero we increase the left pointer
                l += 1
            else:
                res.append([nums[l], nums[r], a]) # if sum is exactly 0 we add a, nums[i] and nums[l] to our result list
                l += 1  # we increment the left pointer
                while nums[l] == nums[l - 1] and l < r: # here we check if the next element is same, and we skip if it
                    # is the same.
                    l += 1
    return res
    return res


# testing
n = [-1, 0, 1, 2, -1, -4]
print("List: ", n)
print(threeSum(self, n))

n2 = [0, 1, 1]
print("List: ", n2)
print(threeSum(self, n2))

n3 = [0, 0, 0]
print("List: ", n3)
print(threeSum(self, n3))
