import numpy as np
def smallest(arr,k):
    flattened=arr.flatten()
    flattened.sort()
    return (flattened[k-1])
nums=np.array([[1,5,9],[10,11,13],[12,13,15]])
k=int(input("kth element:"))
print(smallest(nums,k))
