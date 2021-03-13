class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        aset = set()
        for i in range(len(s) - k + 1):
            aset.add(s[i: i+k])
        return len(aset) == 2**k
