# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
import self as self

# We will use TWO different approaches.

# FIRST APPROACH
# In this approach we check if the string is empty, if yes return true
# we get all alphanumeric characters and put them in one string.
# we check if the string of alphanumeric characters is same to its reverse string then return bool.
# this approach we have to time complexity of O(n) but we are using extra space.
def isPalindrome(self, s: str) -> bool:
    if len(s) == 1:
        return True
    str = ""
    for x in s:
        if x.isalnum() == True:
            str = str + x.lower()
    return str == str[::-1]

# SECOND APPROACH
# In this approach we use two pointers, left and right and try to eliminate the extra use of the space. if the
# character in the left pointer is not alphanumeric we increase the pointer, while Left pointer < right pointer if
# the character in the right pointer is not alphanumeric we decrease the pointer, while Left pointer < right pointer
# And we check if character at left pointer is equal to character at right pointer, if they are not equal we return
# false. If they are equal then increase left pointer and decrease right pointer to check other pairs of characters.

def isPali_twoPointer(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alnumcheck(self, s[l]):
            l += 1
        while r > l and not alnumcheck(self, s[r]):
            r -= 1
        if s[l].lower != s[r].lower:
            return False
        l, r = l + 1, r - 1
    return True


# this function will just tell us if the passed character is alphanumeric or not.
# we check if the ASCII value of c is in between A-Z or a-z or 0-9.
def alnumcheck(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


# our testing strings
s = "mam"
t = ""
c = "carrae"
r = "12@nannan21"

print("Using first approach")
print(isPalindrome(self, s))
print(isPalindrome(self, t))
print(isPalindrome(self, c))
print(isPalindrome(self, r))

print("Using second approach")
print(isPali_twoPointer(self, s))
print(isPali_twoPointer(self, t))
print(isPali_twoPointer(self, c))
print(isPali_twoPointer(self, r))
