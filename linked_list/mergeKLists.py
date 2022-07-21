# Definition for singly-linked list.
from operator import le
from typing import List, Optional
import heapq


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        head = []
        # 优先级队列，最小堆
        # 将 k 个链表的头结点加入最小堆
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            # 获取最小节点，接到结果链表中
            val, index = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[index]:
                heapq.heappush(head, (lists[index].val, index))
                lists[index] = lists[index].next
        return dummy.next
