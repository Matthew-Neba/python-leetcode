
# Key to this problem is realizing the choice of always using the star as a closed bracket can not be wrong since it can be corrected further down the line. 

# O(n) time complexity and O(1) space complexity
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # track open brackets currently encountered and decrement them when we encounter a closed 
        # bracket or star
        opening_found = 0
        closing_used = 0
        opening_available = 0

        for char in s:
            # increment open bracket count
            if char == "(":
                opening_found += 1

            # If we see a star, decrement opening if available and add to closing_used,
            # else increment opening_available
            if char == "*":
                if opening_found > 0:
                    opening_found -= 1
                    closing_used += 1
                else:
                    opening_available += 1
            
            # If we see a closing bracket, decrement opening if available, else check if
            # closing_used > 0; if so, decrement closing_used and add to opening_available
            if char == ")":
                if opening_found > 0:
                    opening_found -= 1
                elif closing_used > 0:
                    closing_used -= 1
                    opening_available += 1
                elif opening_available > 0:
                    # If no closing_used, check opening_available and decrement if > 0, else return False
                    opening_available -= 1
                else:
                    return False

        # return True if all open brackets are matched
        return True if opening_found == 0 else False