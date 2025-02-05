# a = "" #empty string
# a = "Hello" #string with characters
# a[0] #O(1)
# len(a) #O(1)

# a = a + "Hello" #O(n) and a new string is created
# # str1 = str1 + str2 #O(n) and a new string is created

# ---------------------------------------------------------------------------------------------------

# Problem Statement
# A string is considered a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: After processing, the string becomes "amanaplanacanalpanama", which is a palindrome.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alphaNumbericString = ""
#         for c in s:
#             if c.isalpha() or c.isdigit():
#                 alphaNumbericString += c.lower()
#         if alphaNumbericString == alphaNumbericString[::-1]:
#             return True
#         return False

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alphaNumbericString = ''.join([c.lower() for c in s if c.isalnum()])
#         return alphaNumbericString == alphaNumbericString[::-1]
    

# ---------------------------------------------------------------------------------------------------

# Problem Statement
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# Algorithm for myAtoi(string s):
# Ignore leading whitespace: Read and ignore any leading whitespace characters.
# Check for sign (+ or -):
# If the next character is '-' or '+', read it to determine whether the number is negative or positive.
# If neither is present, assume the number is positive.
# Read numeric characters: Read in the next characters until a non-digit character is encountered or the end of the string is reached. Ignore the remaining characters.
# Convert digits to an integer:
# Example: "123" → 123, "0032" → 32
# If no digits are found, return 0.
# Apply the sign determined in step 2.
# Clamp within 32-bit signed integer range:
# The valid range is [-2³¹, 2³¹ - 1].
# If the integer is less than -2³¹, return -2³¹.
# If the integer is greater than 2³¹ - 1, return 2³¹ - 1.
# Return the integer as the final result.
# Notes:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# Example 1:
# Example 1:
# Input: s = "42"
# Output: 42
# Explanation:
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s = s.lstrip()
#         sign = 1
#         if s == "":
#             return 0
#         if s and s[0] in ['-', '+']:
#             sign = -1 if s[0] == '-' else 1
#             s = s[1:]
#         #read until a non-digit character is encountered
#         str = ""
#         for c in s:
#             if c.isdigit():
#                 str += c
#             else:
#                 break
#         ans = int(str)*sign if str else 0
#         if ans < -2**31:
#             return -2**31
#         if ans > 2**31 - 1:
#             return 2**31 - 1
#         return ans
    
# # ---------------------------------------------------------------------------------------------------
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix