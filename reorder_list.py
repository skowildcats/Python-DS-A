# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev, nex, node = None, None, slow

        while node is not None:
            nex = node.next
            node.next = prev
            prev = node
            node = nex

        first, second = head, prev

        next_hop = first.next

        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop

            next_hop = second.next
            second.next = first
            second = next_hop


# Time Complexity: O(n)
# Space Complexity: O(1)
