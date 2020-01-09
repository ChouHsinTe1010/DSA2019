class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
        if not root.right:
            return 1 + self.minDepth(root.left)
        elif not root.left:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))