"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#设置一个指针不断遍历链表的节点,一个临时变量存储该指针下一步指向的链表,另一个变量则不断添加该指针所在的节点
class Solution(object):
    def reverseList_1pointer(self, head):
        """
        :type head: ListNode
        :rtype
        """
        if head==None or head.next==None:
            return head
        #设置辅助变量newList(保存反转链表)、tmp(用于循环时保存)
        newList = None
        while head:
            tmp = head.next
            head.next = newList
            newList = head
            head = tmp
        return newList
#设置两个指针p和q分别指向当前节点和下一个节点,一个变量存储q指针下一步指向的链表
class Solution(object):
    def reverseList_2pointers(self, head):
    """
    :type head: ListNode
    :rtype
    """ 
        if head==None or head.next==None:
            return head
        p = head
        q = head.next
        p.next = None
        while q:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        return p


## 递归调用
class Solution(object):
    def reverseList_recursive(self,head):
        """
        :type head: ListNode
        :rtype
        """ 
        if head==None or head.next==None:
            return head
        else:
            newList = Solution().reverseList_recursive(head.next)
            head.next.next = head
            head.next = None
        return newList

## 逐个插入法
class Solution(object):
    def reverseList_tailInsert(self, head):
        """使用逐个插入法"""
        if head==None or head.next==None:
            return head
        p = head.next
        while p.next:
            q = p.next
            p.next = q.next
            q.next = head.next
            head.next = q

        p.next = head
        head = p.next.next
        p.next.next = None
        return head
