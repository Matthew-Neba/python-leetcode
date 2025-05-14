from collections import defaultdict

# never have a while loop depending on both the left and right pointers simultaneoulsy if possible, can give issues

# Key to solving this problem is by checking if we have all the characters we need in the window. If not, expand the window to attempt to obtain the characters. Then, if when we have all the characters in the window, shrink the window until this is not the case to get the minimum window that contains all the characters. Originally, was comparing the two hashmaps of the sliding window with the search string but this is inefficient. Can instead just keep track of how many characters we have and need. Both have the same time and space complexity, however, the growth constant is lower for the second method.   

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        search_dict, window_dict = defaultdict(int), defaultdict(int)

        for ch in t:
            search_dict[ch] += 1
        
        l = r = 0

        start = 0
        length = float("infinity")

        have = 0
        need = len(t)

        while (r < len(s)):
            if have < need:
                if window_dict[s[r]] < search_dict[s[r]]:
                    have += 1
                
                window_dict[s[r]] += 1
                r += 1
                continue

            if (r - l) < length:
                start = l
                length = r - l

            window_dict[s[l]] -= 1
            if window_dict[s[l]] < search_dict[s[l]]:
                have -= 1

            l += 1 

        # handle the left pointer while
        while have == need:
            if (r - l) < length:
                start = l
                length = r - l

            window_dict[s[l]] -= 1
            if window_dict[s[l]] < search_dict[s[l]]:
                have -= 1

            l += 1

        if length < float("infinity"):
            return (s[start:start+length])
        else:
            return ""

            
solution = Solution()
print(solution.minWindow("ADOBECODEBANC","ABC"))


            
            
            
            

                





        
        

            


        