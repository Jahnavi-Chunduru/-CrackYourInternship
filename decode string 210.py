class Solution(object):
    def decode_util(self, s, start):
        i = start
        curr_num = 0
        curr_str = ''
        
        while i < len(s):
            if s[i].isdigit():
                curr_num *= 10
                curr_num += int(s[i])
                i += 1
            elif s[i] in lowercase:
                curr_str += s[i]
                i += 1
            elif s[i] == '[':
                bracket_decode, last_idx = self.decode_util(s, i+1)
                curr_str += (curr_num * bracket_decode)
                i = last_idx + 1
                curr_num = 0
            elif s[i] == ']':
                break
            
        return curr_str, i
                
    
    def decodeString(self, s):
        return self.decode_util(s, 0)[0]
