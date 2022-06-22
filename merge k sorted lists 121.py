from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        count = 0
        for l in lists:
            if l:
                q.put((l.val, count, l))
                count += 1
        print (q)
        while not q.empty():
            val, count, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, count, node))
            print (q)
        return head.next
