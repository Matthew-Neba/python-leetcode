from typing import List

# Note that there are exponentially many combinations. backtacking problem. 
# Need to just find the constraints optimally

# Key to this problem is using the mapping dict instead of manually doing the backtracking logic. Using the mapping here just reduces so much branching logic. Always try and generalize complicated branching logic.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(path, choice_idx):
            if choice_idx > len(digits) - 1:
                res.append("".join(path))
                return
            
            for char in mapping[digits[choice_idx]]:
                path.append(char)
                backtrack(path, choice_idx + 1)
                path.pop()

        backtrack([], 0)
        return res



# Complicated branching solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []

        def backtrack(path, choice_idx):
            if choice_idx > len(digits) - 1:
                res.append("".join(path))
                return
            
            choice_digit = digits[choice_idx]
            start_int = None

            if choice_digit == "2":
                start_int = ord("a")

            if choice_digit == "3":
                start_int = ord("d")
            
            if choice_digit == "4":
                start_int = ord("g")

            if choice_digit == "5":
                start_int = ord("j")

            if choice_digit == "6":
                start_int = ord("m")

            if choice_digit == "7":
                start_int = ord("p")

            if choice_digit == "8":
                start_int = ord("t")

            if choice_digit == "9":
                start_int = ord("w")


            # consider all the choices for the current digit
            if choice_digit not in set(["7","9"]):
                for i in range(3):
                    path.append(chr(start_int + i))
                    backtrack(path, choice_idx + 1)
                    path.pop()
            else:
                print(choice_digit)
                for i in range(4):
                    path.append(chr(start_int + i))
                    backtrack(path, choice_idx + 1)
                    path.pop()

        backtrack([], 0)
        return res
        