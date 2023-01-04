# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# Here our goal is to group the anagrams together.
# In this approach we will sort each word from string and group same words together.
# We will use dictionary to store them. Keys will be sorted words from string and values will be the anagrams
# that are in the string list
# Time complexity of this algorithm is  O (m *(n long n)). M is the length of the list,
# n is the length of each string in the list so, n log n time will take to sort each word from string list.
from collections import defaultdict
from typing import List

from self import self


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if len(strs) == 1:                      # if list contains only one word
        return strs
    group = {}
    for word in strs:
        sorted_word = tuple(sorted(word))
        if sorted_word in group:
            group[sorted_word].append(word)
        else:
            group[sorted_word] = [word]
    return list(group.values())             # returning values as list

# SECOND WAY WITH BETTER TIME COMPLEXITY
# here we will try to element the sorting factor and while we are going through the list, group them.
# We will still use dictionary to store grouped anagrams
# We will count the letters in each word from the str list and use it as key to store the values with same number
# letters or anagrams.
# TIME COMPLEXITY IS O(m* n) where n is the  average length of words in strs and m is the length of strs

def secondWay(self, strs: List[str]) -> List[List[str]]:
    if len(strs) == 1:
        return strs
    group = defaultdict(list)                       # defaultdict never raises the KeyError, if key does not exist
    #group= {}
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        group[tuple(count)].append(word)           # we can not use list as key so, we turn it into tuple.
    return list(group.values())                    # Typecasting to list ot match the output format


# Testing
strs1 = [""]
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(self, strs))
print(groupAnagrams(self, strs1))

print("SECOND WAY ")
print(secondWay(self, strs))
print(secondWay(self, strs1))
