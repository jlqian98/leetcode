# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        给你一个链表的头节点 head ，判断链表中是否有环。
        如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        p, q = head, head.next
        while p != None and q != None and q.next != None:
            if p == q:
                return True
            p = p.next
            q = q.next.next
        return False