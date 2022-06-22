def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map_ = {}
        node = head
        
        while True:
            if node is None:
                break

            map_[node] = Node(node.val, node.next, node.random)
            node = node.next 

        for node in map_:
            if node.next is not None:
                map_[node].next = map_[node.next]
            
            if node.random is not None:
                map_[node].random = map_[node.random]

        return map_.get(head)
