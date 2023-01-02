# Given an integer array nums and an integer k, return the k most frequent elements. You may return
# the answer in any order.
# Here we are trying to find the k most frequent elements, i.e. if k is 2 then we are trying to find 2 most
# frequent values.
# if array is [1,1,5,5,5,6,6,6,6] and k is 2 we are going to return [5,6]
# because 5 occurs 3 times and 6 occurs 4 times
import operator

# Here is simple solution
# we make dictionary and count the occurrence of each element then
# we sort the dictionary based upon the values in decreasing order
# time complexity of this algorithm is O(nlog n)
def firstWay(nums:list[int], k: int):
    d = {}
    for n in nums:
        d[n] = 1 + d.get(n, 0)
    sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted_dict)
    keylist=[]
    for x in sorted_dict.keys():
        keylist.append(x)
    print(keylist)
    return keylist[:k]

# SECOND WAY WITH TIME COMPLEXITY OF O(n).
# Here time complexity of our algorithm must be O(n).
# We can use dictionary to figure out the occurrences of each element
# And we will make an array of size len(nums) + 1 where we will use occurrence as indices and list of numbers with same
# occurrence as values.



# Testing

n = [1,1,1,2,2,3,3,3,3]
k = 2
print("First way with time complexity of the O(n log n) ")
print(firstWay(n, k))

print("Second way with the time complexity of O(n)")
