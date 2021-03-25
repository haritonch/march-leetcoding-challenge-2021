class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: 
            return []
        
        n, m = len(matrix), len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(row, col, reachable):
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_col = row + x, col + y
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue
                if (new_row, new_col) in reachable:
                    continue
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                dfs(new_row, new_col, reachable)
        
        for i in range(n):
            dfs(i, 0, pacific_reachable)
            dfs(i, m - 1, atlantic_reachable)
        for i in range(m):
            dfs(0, i, pacific_reachable)
            dfs(n - 1, i, atlantic_reachable)
        
        return list(pacific_reachable.intersection(atlantic_reachable))