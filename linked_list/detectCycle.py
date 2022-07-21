"""
142. 环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        # 思路：快慢指针，快慢相遇之后，其中一个指针回到头，快慢指针步调一致一起移动，相遇点即为入环点
        if head is None:
            return head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 指针重新从头开始移动
                fast = head
                # 比较指针对象（不要比对指针Val值）
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        # 思路：快慢指针，快慢相遇之后，慢指针回到头，快慢指针步调一致一起移动，相遇点即为入环点
        if head is None:
            return head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 慢指针重新从头开始移动，快指针从第一次相交点下一个节点开始移动
                slow = head
                # 比较指针对象（不要比对指针Val值）
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None


# 坑点

# 指针比较时直接比较对象，不要用值比较，链表中有可能存在重复值情况
# 第一次相交后，快指针需要从下一个节点开始和头指针一起匀速移动
# 注意，此题中使用 slow = fast = head 是为了保证最后找环起始点时移动步数相同，但是作为找中点使用时一般用 fast=head.Next 较多，因为这样可以知道中点的上一个节点，可以用来删除等操作。

# fast 如果初始化为 head.Next 则中点在 slow.Next
# fast 初始化为 head,则中点在 slow