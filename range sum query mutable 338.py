class FenwickTree:
    def __init__(self, arr):                        
        self.build(arr)
        
    def build(self, arr):        
        self.original = arr
        self.tree = [0]  + arr.copy()
        for idx in range(1, len(self.tree)):
            parent = idx + self.rsb(idx) 
            if parent < len(self.tree):
                self.tree[parent] += self.tree[idx]            
    def add(self, idx, delta):        
        while idx < len(self.tree):            
            self.tree[idx] += delta
            idx += self.rsb(idx)
    def sum(self, idx):
        res = 0
        while 0 < idx:
            res += self.tree[idx]
            idx -= self.rsb(idx)
        return res
    def rsb(self, idx):
         return idx & (-idx)
    def update(self, i, val):
        self.add(i + 1, val - self.original[i])
        self.original[i] = val
    def query(self, i, j):
        return self.sum(j + 1) - self.sum(i)            
        
class NumArray:

    def __init__(self, nums: List[int]):        
        self.tree = FenwickTree(nums)        

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:        
        return self.tree.query(left, right)
