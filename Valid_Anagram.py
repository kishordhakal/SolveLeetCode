# Leet code valid anagram

# given two strings we have to find if they are anagrams or not
# An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original
# letters exactly once.

# first Approach we use two dictionaries (hash map in python) to store each letters of two strings
# and check if both hashmaps are same.
# time complexity will be O(N)
def IsAnagream(s: str, t: str):
    # check if the strings are of different lengths then they are not anagrams
    if len(s) != len(t):
        return False
    # create two dictionary
    smap = {}
    tmap = {}
    # key is the letter and the value is the count
    # iterate though the both strings and store the letter count in both dictionary
    for i in range(len(s)):
        # here we count the letters and their numbers of occurrence
        # for string s
        smap[s[i]] = 1 + smap.get(s[i], 0)
        # for string t
        tmap[t[i]] = 1 + tmap.get(t[i], 0)

    # now we check the if both of dictionary contains the same key and value
    for x in smap:
       # print("smap ",smap[x])
       # print("tmap ", tmap.get(x, 0))
        if smap[x] != tmap.get(x, 0):
            return False
    return True
# sort the stings in alphabetical order using inbuilt sort function
# Time complexity will be the time complexity of  sort() in Python
# Its time complexity is O(NlogN).
def sortedWay(s: str, t: str):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# test case
s = "@elloy"
t = "olle@o"

# calling function and printing outputs
print("First Approach using dictionary")
print(IsAnagream(s, t))
print("Second Approach using inbuilt sort function")
print(sortedWay(s, t))
