# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(min_num, max_num):
            # 临界点
            if min_num > max_num:
                return [None,]
            ans = []    # 所有满足条件的树
            for num in range(min_num, max_num+1):
                # ---分----
                left = generate(min_num, num-1)     # 所有左子树
                right = generate(num+1, max_num)    # 所有右子树
                
                # ---治----
                for l in left:
                    for r in right:
                        root = TreeNode(num)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        return generate(1, n)