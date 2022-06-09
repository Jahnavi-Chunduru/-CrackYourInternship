class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(lambda : 0)
        left = 0
        max_frequency = float('-infinity')
        max_window = 0
        
        for right in range(len(s)):
            
            counter[s[right]] += 1
            current_window = right - left + 1
            if counter[s[right]] > max_frequency:
                max_frequency = counter[s[right]]
            
            while current_window - max_frequency > k:
                counter[s[left]] -= 1
                current_window -= 1
                left += 1
				
            if max_window < current_window:
                max_window = current_window
        
        return max_window
