class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        st1 = []
        st2  =[]
        cur = head
        
        while cur is not None:
            st1.append(cur)
            cur=cur.next
            
        while st1:
            ins_flag = True
            node = st1.pop()
            
            
            while st1 and st1[-1].val == node.val:
                ins_flag = False
                st1.pop()
            
            if ins_flag:
                st2.append(node)
            
        
        
            
                
        point = head = ListNode(0)
        
        while st2:
            point.next = st2.pop()
            point = point.next
        
        point.next = None
        return head.next
