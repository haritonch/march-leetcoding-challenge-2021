from collections import defaultdict

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        M = 10**9 + 7
        ones = defaultdict(int)
        twos = defaultdict(int)
        
        for i, num in enumerate(arr):
            ans = (ans + twos[target - num]) % M
            for one, count in ones.items():
                twos[num + one] += count
            ones[num] += 1
        return ans