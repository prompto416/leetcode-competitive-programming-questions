class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth( root):
    if not root:
        return 0
    """
    :type root: TreeNode
    :rtype: int
    """

    return 1 + max((maxDepth(root.left)),maxDepth(root.right))
    
    
a = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))

print(maxDepth(a))

#to submit you need this 
# def maxDepth(self, root):
#         if not root:
#             return 0
#         """
#         :type root: TreeNode
#         :rtype: int
#         """

#         return 1 + max((self.maxDepth(root.left)),self.maxDepth(root.right))