class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = head
        if head==None:
            return None
        
        if head.child:
            t = head.next
            node = self.flatten(head.child)
            head.next = node
            head.child=None
            node.prev = head
            while node.next:
                node = node.next
            node.next = t
            if t:
                t.prev = node
        
        self.flatten(head.next)
        return h
