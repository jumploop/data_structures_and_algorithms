"""

138. 复制带随机指针的链表


给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 思路：1、hash 表存储指针，2、复制节点跟在原节点后面
        if head is None:
            return head
        # 复制节点，紧挨到到后面
        # 1->2->3  ==>  1->1'->2->2'->3->3'
        cur = head
        while cur:
            clone = Node(x=cur.val, next=cur.next)
            tmp = cur.next
            cur.next = clone
            cur = tmp
        # 处理random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 分离两个链表
        cur = head
        cloneHead = cur.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            cur = tmp
        # 原始链表头：head 1->2->3
        # 克隆的链表头：cloneHead 1'->2'->3'
        return cloneHead