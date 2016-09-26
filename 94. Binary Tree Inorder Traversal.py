# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder(result,root)
        return result
    
    def inorder(self,result,root):
        if root == None:
            return
        self.inorder(result,root.left)
        result.append(root.val)
        self.inorder(result,root.right)
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        result = []
        stack = [root]
        visit = {}
        while len(stack) != 0:
            curr = stack.pop()
            if curr in visit:
                result.append(curr.val)
                continue
            else:
                visit[curr] = 1
            if curr.right != None:
                stack.append(curr.right)
            stack.append(curr)
            if curr.left != None:
                stack.append(curr.left)
        return result
        
        
            
            