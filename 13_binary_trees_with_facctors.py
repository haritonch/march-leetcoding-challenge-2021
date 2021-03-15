class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {el: 1 for el in arr}
        arr.sort()
        for i, x in enumerate(arr):
            for y in arr[:i]:
                if x % y == 0 and x // y in arr:
                    dp[x] += dp[y] * dp[x // y]
        
        return sum(dp.values()) % (10**9 + 7)