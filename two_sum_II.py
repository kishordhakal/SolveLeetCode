# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers
# be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer
# array [index1, index2] of length 2. The tests are generated such that there is exactly one solution.
# You may not use the same element twice.Your solution must use only constant extra space.

# THINGS TO REMEMBER
# Array is 1-indexed and sorted in non-decreasing order,  Allowed only constant extra space
# We can use the two pointers left (pointing first element ) and right(pointing last element).
# We calculate the sum and compare it with  target
# If the sum > target  we decrease the right pointer by 1 and if sum < target increase the left pointer by 1
# another condition is  sum == target and here we return left and right pointer.
from typing import List

from self import self


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # Two pointers
    l, r = 0, len(numbers)-1

    while l < r :
        sum= numbers[l]+ numbers[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l +=1
        else:
            return [l+1, r+1]    # remember our array is 1-indexed
    return []                    # If the given list has no solution

#testing
# all these test cases has exactly one solution
list1 = [2, 7, 11, 15]
target1 = 9
list2 = [2, 3, 4]
target2 = 6
list3 = [-1, 0]
target3 = -1

print(twoSum(self, list1, target1))
print(twoSum(self, list2, target2))
print(twoSum(self, list3, target3))


