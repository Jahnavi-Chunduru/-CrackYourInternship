class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d=dict()
        while(headA!=None):
            d[headA]=1
            headA=headA.next
        while(headB!=None):
            if(headB in d.keys()):
                return headB
            headB=headB.next
        return None
