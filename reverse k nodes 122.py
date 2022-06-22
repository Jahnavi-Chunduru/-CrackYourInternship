class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse_list(head,k):
            cur, prev = head, None
            
            while k:
                next_node = cur.next
                
                cur.next = prev
                prev = cur
                cur = next_node
                k -= 1
            
            return prev
        
        def helper(head,k):
            count = 0
            cur = head
            
            while count < k and cur:
                cur = cur.next
                count += 1
            
            if count == k:
                last_node = reverse_list(head, k)
                
                head.next = helper(cur, k)
            
                return last_node
            
            return head
        
        return helper(head,k)
