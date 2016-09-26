# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorder(result,root)
        return result
        
    def preorder(self,result,root):
        if root == None:
            return 
        result.append(root.val)
        self.preorder(result,root.left)
        self.preorder(result,root.right)
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        result = []
        stack = [root]
        while len(stack) != 0:
            temp = stack.pop()
            result.append(temp.val)
            if temp.right != None:
                stack.append(temp.right)
            if temp.left != None:
                stack.append(temp.left)
        return result
        