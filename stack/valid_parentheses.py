class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
        }

        for bracket in s:
            if bracket in pairs.values():
                # open bracket
                stack.append(bracket)
            else:
                # closed bracket
                if stack and stack[-1] == pairs[bracket]:
                    stack.pop()
                else:
                    # excess close brackets
                    return False
        
        # make sure no excess open brackets
        return len(stack) == 0
