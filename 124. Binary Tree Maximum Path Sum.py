class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathsum = float("-inf")

        def dfs(node):
            if node is None:
                return 0
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            total_sum = left_sum + right_sum + node.val
            
            # update global max
            self.pathsum = max(self.pathsum, total_sum)

            # return max gain to parent
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.pathsum
