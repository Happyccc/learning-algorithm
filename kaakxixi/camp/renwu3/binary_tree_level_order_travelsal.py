"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""采用深度优先搜索"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = []   #构建队列
        queue.append(root) #添加树
        res = [] #结果列表
 
        while queue:
            nodes = [] #每次循环开始清空节点列表
            vals = [] #每层的节点值
 
            for i in queue:
            #先找左子树，左子树不为空，添加到节点列表中
                if i.left:
                    nodes.append(i.left)
            #再找右子数
                if i.right:
                    nodes.append(i.right)
            # 节点值
                vals += [i.val]
            # 把下一层的节点列表赋给队列
            queue = nodes
            res = [vals] + res  #结果列表：汇总各层节点值列表
        return res
       
        
