class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        p1,p2 = head,head.next
        val1 = 0
        
        while p2 and p2.next:
            val1 =val1*10+p1.val
            p1 = p1.next
            p2 = p2.next.next
        if p2:
            val1=val1*10+p1.val
        p1 = p1.next
        val2=  0
        mult=1
        while p1:
            val2 = p1.val*mult+val2
            p1 = p1.next
            mult*=10
        return val1 == val2
	
