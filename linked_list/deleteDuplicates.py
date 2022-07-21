#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current = head
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head



