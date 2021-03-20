class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we use Gauss' formula
        n = len(nums)
        s = sum(nums)
        return n * (n+1) // 2 - s
