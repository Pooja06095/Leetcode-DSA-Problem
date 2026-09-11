# LeetCode 222 - Count Complete Tree Nodes
# Time: O(log^2 n)
# Space: O(log n)

class Solution:
    def countNodes(self, root):
        if root is None:
            return 0

        left = root
        right = root

        left_height = 0
        right_height = 0

        while left:
            left_height += 1
            left = left.left

        while right:
            right_height += 1
            right = right.right

        # If both heights are same, tree is a perfect binary tree
        if left_height == right_height:
            return (1 << left_height) - 1

        # Otherwise, count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)