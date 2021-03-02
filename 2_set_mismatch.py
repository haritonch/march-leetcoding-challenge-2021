class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = {i: 0 for i in range(1, n+1)}
        for num in nums:
            f[num] += 1
        duplicate, missing = -1, -1
        for num in range(1, n+1):
            if f[num] == 0:
                missing = num
            elif f[num] == 2:
                duplicate = num
        return [duplicate, missing]
