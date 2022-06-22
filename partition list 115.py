class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return
        curr, lyst =head, []
        while curr:
            if curr.val < x:
                lyst.append(curr)
            curr = curr.next
            
        curr = head
        while curr:
            if curr.val >= x:
                lyst.append(curr)
            curr = curr.next
                
        for i in range(len(lyst)):
            if i == len(lyst)-1:
                lyst[i].next = None
                break
            lyst[i].next = lyst[i+1]
            
        temp = lyst[0]
        del lyst
        return temp
