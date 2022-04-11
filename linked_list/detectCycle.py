#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 8:38
# @Author  : 一叶知秋
# @File    : detectCycle.py
# @Software: PyCharm
"""
142. 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。



示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

"""


# 思路：快慢指针，快慢相遇之后，慢指针回到头，快慢指针步调一致一起移动，相遇点即为入环点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 思路：快慢指针，快慢相遇之后，快指针回到头，快慢指针步调一致一起移动，相遇点即为入环点
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                # 快指针重新从头开始移动，慢指针从第一次相交点下一个节点开始移动
                fast = head
                slow = slow.next
                # 注意 比较指针对象（不要比对指针Val值）
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
            fast, slow = fast.next.next, slow.next
        return None
        #   坑点
        #
        # 指针比较时直接比较对象，不要用值比较，链表中有可能存在重复值情况
        # 第一次相交后，快指针需要从下一个节点开始和头指针一起匀速移动

    def detectCycle2(self, head: ListNode) -> ListNode:
        # 思路：快慢指针，快慢相遇之后，其中一个指针回到头，快慢指针步调一致一起移动，相遇点即为入环点
        if not head:
            return head
        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                # 指针重新从头开始移动
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None

    def detectCycle3(self, head: ListNode) -> ListNode:
        # 思路:哈希表
        visited = set()
        node=head
        while node:
            if node in visited:
                return node
            visited.add(node)
            node=node.next
        return None

'''
算法

首先，我们分配一个 Set 去保存所有的列表节点。我们逐一遍历列表，检查当前节点是否出现过，如果节点已经出现过，那么一定形成了环且它是环的入口。否则如果有其他点是环的入口，我们应该先访问到其他节点而不是这个节点。其他情况，没有成环则直接返回 null 。

算法会在遍历有限个节点后终止，这是因为输入列表会被分成两类：成环的和不成环的。一个不成欢的列表在遍历完所有节点后会到达 null - 即链表的最后一个元素后停止。一个成环列表可以想象成是一个不成环列表将最后一个 null 元素换成环的入口。

如果 while 循环终止，我们返回 null 因为我们已经将所有的节点遍历了一遍且没有遇到重复的节点，这种情况下，列表是不成环的。对于循环列表， while 循环永远不会停止，但在某个节点上， if 条件会被满足并导致函数的退出。

作者：LeetCode
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''