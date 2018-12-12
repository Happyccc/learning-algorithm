"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""快速排序 """
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tail = self.get_tail(head)
        head, tail = self.quick_sort(head, tail)
        tail.next = None
        return head
 
    def quick_sort(self, head, tail):
        """
        Sort in place
        :param head:
        :param tail:
        :return:
        """
        if head is not tail:
            head_left, tail_left, head_ref, tail_ref, head_right, tail_right = self.quicksort_partition(head, tail)
            if head_left is None:  # if there is no node in left part after partition
                head = head_ref
            else:
                head_left, tail_left = self.quick_sort(head_left, tail_left)
                head = head_left
                tail_left.next = head_ref
            if head_right is None:  # if there is no node in right part after partition
                tail = tail_ref
            else:
                head_right, tail_right = self.quick_sort(head_right, tail_right)
                tail_ref.next = head_right
                tail = tail_right
        return head, tail
 
 
    def quicksort_partition(self, head, tail):
        reference = tail
        head_ref, tail_ref = reference, reference
        head_left, tail_left, head_right, tail_right = None, None, None, None
 
        sentinel = ListNode(None)  # use sentinel to simplify the code
        sentinel.next = head
        node = sentinel
        while node.next is not tail:
            node = node.next
            if node.val > reference.val:  # put node into right part
                if head_right is not None:
                    tail_right.next = node
                    tail_right = node
                else:  # right part is empty
                    head_right = node
                    tail_right = node
            elif node.val < reference.val:  # put node into left part
                if head_left is not None:
                    tail_left.next = node
                    tail_left= node
                else:  # left part is empty
                    head_left = node
                    tail_left = node
            else:  # put node into reference part
                tail_ref.next = node
                tail_ref = node
        return head_left, tail_left, head_ref, tail_ref, head_right, tail_right
 
    def get_tail(self, node):
        while node.next:
            node = node.next
        return node
