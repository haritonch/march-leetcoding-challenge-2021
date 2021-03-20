# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans = []
        frontier = [root]
        while frontier:
            ans.append(float(sum([node.val for node in frontier]) / len(frontier)))
            new_frontier = []
            for node in frontier:
                if node.left:
                    new_frontier.append(node.left)
                if node.right:
                    new_frontier.append(node.right)
            frontier = new_frontier
        return ans