from collections import dequeue
class stack(object):
    def __init__(self):
        self.queue=dequeue()
    def push(self,x):
        self.queue.append(x)
    def pop(self):
        ql=len(self.queue)
        for i in range(ql-1):
            x=self.queue.popleft()
            self.queue.append(x)
        self.queue.popleft()
    def top(self):
        ql=len(self.queue)
        for i in range(ql):
            x=self.queue.popleft()
            self.queue.append(x)
        return x
    def empty(self):
        return(bool(self.queue))
