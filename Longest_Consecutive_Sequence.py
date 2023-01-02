# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# We should remember that our algorithm should run in O(n) so iterating through it twice or sorting it is not an option
# Here one trick we can use is saving the array somewhere and while iterating through the array we check for
# element that might make sequence with the number at index i.
# we can use set to store the elements and to look up for elements.
# whenever we are looking at number from an array we see if the array has previous number.

from typing import List

from self import self


def longestConsecutive(self, nums: List[int]) -> int:
    numset = set(nums)
    longest = 0
    length = 0
    for i in nums:
        if (i-1) not in numset:
            while(i+length) in numset:
                length += 1
            longest = max(length, longest)
    return longest


# Testing
n = [100, 4, 200, 1, 3, 2]

print(longestConsecutive(self, n))
