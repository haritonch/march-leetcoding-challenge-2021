class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for center in range(n):
            for (l, r) in ((center, center), (center, center+1)):
                while l >= 0 and r < n:
                    if s[r] == s[l]:
                        ans += 1
                        r += 1
                        l -= 1
                    else:
                        break
        return ans
