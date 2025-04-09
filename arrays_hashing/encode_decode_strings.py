from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str: 
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#"
            encoded_string += s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:

        strs = []
        cur_idx = 0

        while cur_idx < len(s) - 1:
            
            cur_len_str = ""

            while s[cur_idx] != "#":
                cur_len_str += s[cur_idx]
                cur_idx += 1

            
            str_len = int(cur_len_str)
            cur_idx += 1

            curStr = s[cur_idx:cur_idx+str_len]
            strs.append(curStr)

            cur_idx += str_len

        return strs 


solution = Solution()

print(solution.decode(solution.encode(["we","say",":","yes","!@#$%^&*()"])))

