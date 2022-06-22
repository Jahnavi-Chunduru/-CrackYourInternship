class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        lyst, cur = [], head
        while cur:
            lyst.append(cur)
            cur = cur.next
        l,r = 0,len(lyst)-1
		
		# when l and r ptrs cross, we are done, lyst[l] is at tail
        while l < r:
            lyst[l].next = lyst[r]
            l += 1
            lyst[r].next = lyst[l]
            r -= 1
            
        lyst[l].next = None
        return lyst[0]
