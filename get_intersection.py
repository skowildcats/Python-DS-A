class Solution:
    def changeSign(self, head):
        while head:
            head.val = -head.val
            head = head.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        self.changeSign(headA)

        while headB:
            if headB.val < 0:
                break
            headB = headB.next

        self.changeSign(headA)
        return headB
