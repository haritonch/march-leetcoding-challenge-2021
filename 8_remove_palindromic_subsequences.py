class Solution:
    def removePalindromeSub(self, s: str) -> int:
        palindrome = lambda s: all(s[i] == s[-i-1] for i in range(len(s) // 2))
        if not s:
            return 0
        elif palindrome(s):
            return 1
        else:
            return 2
