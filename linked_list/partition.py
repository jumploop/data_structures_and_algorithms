"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
from binhex import LINELEN
from multiprocessing import dummy


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        # 思路：将大于x的节点，放到另外一个链表，最后连接这两个链表
        if head is None:
            return head
        headDummy = ListNode()
        tailDummy = ListNode()
        tail = tailDummy
        headDummy.next = head
        head = headDummy
        while head.next:
            if head.next.val < x:
                head = head.next
            else:
                # 移除<x节点
                tmp = head.next
                head.next = head.next.next
                # 放到另外一个链表
                tail.next = tmp
                tail = tail.next
        # 拼接两个链表
        tail.next = None
        head.next = tailDummy.next
        return headDummy.next
