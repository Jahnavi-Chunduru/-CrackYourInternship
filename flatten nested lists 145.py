import numpy as np
print("enter the elements of array")
nums=[[1,1],[2],[1,1]]
flatnums=list(np.concatenate(nums).flat)
print(flatnums)
