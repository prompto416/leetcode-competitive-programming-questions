def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        myDict = dict()
        
        def dfs(node,level):
            if not node: return
            if level not in myDict:
                myDict[level] = []
            myDict[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        
        dfs(root,0)
        print(myDict)
       
        return myDict.values()