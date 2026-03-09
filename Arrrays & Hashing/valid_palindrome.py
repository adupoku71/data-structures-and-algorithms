"""Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true"""

# Time: O(n) Space: O(n)
def isPalindrome(s):
        new_string = ''
        for char in s:
            new_string += char if char.isalnum() else ""
        new_string = new_string.lower()

        return new_string == new_string[::-1]