"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 思路：先遍历到 m 处，翻转，再拼接后续，注意指针处理
        if head is None:
            return head
        right -= left  # number of times of reverse
        curr = dummy = ListNode(next=head)
        while left > 1:  # find node at m - 1
            curr = curr.next
            left -= 1

        start = curr.next
        while right > 0:  # reverse n - m times
            tmp = start.next
            start.next = tmp.next
            tmp.next = curr.next
            curr.next = tmp
            right -= 1
        return dummy.next

    