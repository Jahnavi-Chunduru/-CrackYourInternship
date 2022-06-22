class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None:
            return head
        curr = head
        start = head
        count = 1
        while(count < left):
            start = curr  
            curr = curr.next
            count += 1
        tail = curr
        prev = None
        while count < right:
            
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            count += 1 
        nodes = curr.next
        curr.next = prev
        prev = curr
        start.next = curr
        tail.next = nodes
        if left > 1:
            return head
        return prev
