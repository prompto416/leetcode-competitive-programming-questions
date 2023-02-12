class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def myinorder(root):
            if not root:
                return 
            myinorder(root.left)
            res.append(root.val)
            myinorder(root.right)
        myinorder(root)


        return res    