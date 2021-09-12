# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        reversed_list = None

        while fast is not None and fast.next is not None:
            tmp = slow

            slow = slow.next
            fast = fast.next.next

            tmp.next = reversed_list
            reversed_list = tmp

        if fast is not None:
            slow = slow.next

        while slow is not None:
            if slow.val != reversed_list.val:
                return False
            else:
                slow = slow.next
                reversed_list = reversed_list.next
        return True


# Time Complexity: O(n)
# Space Complexity: O(1)
# use slow and fast pointers to find middle of a singly linked list,
# keep track of a reversed linked-list up until slow and compare reversed list
# with slow going forward
