def mostCompetitive(self, nums, k):
    remove_num_elements = len(nums) - k
    
    stack = []
    
    for index, num in enumerate(nums):
        while stack and remove_num_elements and nums[stack[-1]] > nums[index]:
            stack.pop()
            remove_num_elements -= 1
            
        stack.append(index)
    
    return [nums[i] for i in stack][:k]
