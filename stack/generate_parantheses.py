from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 
        # Just a backtracking problem. We need a list of lists that we must
        # construct individually, perfect for backtracking.
        #

        res = []
        def backtrack(path, open_brack, close_brack):

            # base case
            if len(path) == n * 2:
                res.append("".join(path[:]))
                return
 
            # see if we can add an open bracket
            if open_brack < n:
                path.append("(")
                backtrack(path, open_brack + 1, close_brack)

                # undo choise
                path.pop()
            
            # see if we can add a closing bracket
            if open_brack > close_brack and close_brack < n:
                path.append(")")
                backtrack(path, open_brack, close_brack + 1)
                
                # undo choise
                path.pop()
        
        backtrack([],0,0)
        return res
            

