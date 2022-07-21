"""
141. 环形链表

给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 思路2：快慢指针，快慢指针相同则有环，证明：如果有环每走一步快慢指针距离会减 1，空间复杂度 O(1) 最优，时间复杂度 O(n) 但循环次数小于等于 n
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # 思路：快慢指针 快慢指针相同则有环，证明：如果有环每走一步快慢指针距离会减1
        if head is None:
            return False
        fast=head.next
        slow=head
        while fast and fast.next:
            # 比较指针是否相等（不要使用val比较！）
            if fast==slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False