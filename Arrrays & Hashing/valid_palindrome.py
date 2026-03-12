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

#Time: O(n) Space: O(1)    
def isPalindromeOptimised(s):
    n = len(s)
    l = 0
    r = n - 1
    
    while r > l:
        while r > l and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
            
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == '__main__':
    sentence = "..  $$aba aba ??"
    print(isPalindrome(sentence))
    print(isPalindromeOptimised(sentence))