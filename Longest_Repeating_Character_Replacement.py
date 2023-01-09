# You are given a string s and an integer k. You can choose any character of the string and change it to
# any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after
# performing the above operations.
from self import self

def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        maxCount = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxCount = max(maxCount, count[s[r]])
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result



# testing
s="AABABBA"
k = 1
print(characterReplacement(self, s, k))