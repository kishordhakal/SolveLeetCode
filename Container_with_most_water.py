# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).Find two lines that together with the x-axis form a container,
# such that the container contains the most water.Return the maximum amount of water a container can store.

# Here we will calculate what amount of water each possible container can hold and pick the container that can hold
# maximum amount of the water


# We have to iterate though the two elements of array at the same time to make a container One efficient
# way to do it is, using two pointer so our algorithm will have a time complexity of O(n)

# The way to calculate the amount of water each container can hold is
# (right pointer - left pointer) * minimum of the element pointed by any of those pointers.
# Here we have to use min because container can't be slanted
# each time we will compare and update  the container that can hold maximum amount of water if found.
# Each time we update the left pointer when element at right pointer is greater because we are trying to find the container
# with maximum capacity.


from typing import List

from self import self


def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height)-1
    maxWaterCapacity= 0
    while l < r :
        currentContainerCapacity= min(height[l], height[r]) * (r-l)
        maxWaterCapacity= max(currentContainerCapacity, maxWaterCapacity)
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    return maxWaterCapacity

# Testing
height =[ 1, 8, 6, 2, 5, 4, 8, 3, 7 ]

print(maxArea(self, height))




