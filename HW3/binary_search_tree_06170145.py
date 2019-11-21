class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val:
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insert(root.left, val)
            elif root.val < val:
                if root.right is None:
                    root.right=TreeNode(val)
                else:
                    self.insert(root.right, val)
            else:
                temp = TreeNode(val)
                temp.left=root.left
                root.left=temp
        else:
            root.val=val

        

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if root == None:
            return None
        elif root.val == target:
            if root.left == None:
                if root.right == None:
                    return None
                else:
                    return root.right
            else:
                if root.right == None:
                    if root.left.val == target:
                        root.left = self.delete(root.left, target)
                    return root.left
                else:
                    if root.left.val == target:
                        root.left = self.delete(root.left, target)
                    cur = cur.right
                    while cur.left != None:
                        cur=cur.left
                    root.val = cur.val
                    cur.val = target
                    root.right = self.delete(root.right, target)
        elif root.val > target:
            root.left = self.delete(root.left, target)
        else:
            root.right = self.delete(root.right, target)
        return root

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root:
            if root.val is target:
                return root
            if root.left:
                temp=self.search(root.left, target)
                if temp is not None:
                    return temp
            if root.right:
                return self.search(root.right, target)


    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        cnt=[0]
        def dfs_cnt(root, target):
            if root:
                if root.val == target:
                    cnt[0] = cnt[0]+1
                dfs_cnt(root.left, target)
                dfs_cnt(root.right, target)
        dfs_cnt(root, target)
        self.delete(root, target)
        for i in range(cnt[0]):
            self.insert(root, new_val)

'''內容參考資料https://www.youtube.com/watch?v=YlgPi75hIBc&t=131s
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
https://emn178.pixnet.net/blog/post/94574434
http://squall.cs.ntou.edu.tw/cpp/103spring/labtest/test1/BinarySearchTree.html
http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html'''