class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)
        # list of elements in a that are greater than a given b of B
        greater_than = {b: [] for b in B} 
        # elements to use when an a is not useful
        rest = [] 
        n = len(A)
        j = 0
        for a in sortedA:
            b = sortedB[j]
            if a > b:
                greater_than[b].append(a)
                j += 1
            else:
                rest.append(a)
        
        return [greater_than[b].pop() if greater_than[b] else rest.pop() for b in B]
