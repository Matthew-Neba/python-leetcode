
# Key to this problem is realizing that we already know how to handle the open and closed brackets if we use a stack (or a regular counter for this problem since there is only one kind of bracket). Thus, the * are the only problem to handle. To handle the star, we realize that if we need to use a star to form a closed bracket, we may potentially need to reverse that operation if we see the matching closed bracket later down the string. If we need an open bracket however, then there is no reversing that operation later down the line.

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