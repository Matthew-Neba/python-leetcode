from typing import List
class Solution:
    # 
    # 
    # In Reverse Polish Notation (RPN), every operator applies to the two most recent numbers
    # (for binary operators like +, -, ×, /). Once you apply the operator, you can think of 
    # it as replacing those two numbers with the result. The operations are applied from left
    # to right
    #
    # ex: 5 2 8 3 + * +   |-->   5 2 11 * +   |-->  5 22 +  --> 27
    #
    def evalRPN(self, tokens: List[str]) -> int:

        cur_elements = []
        operations = set("+-*/")

        for tok in tokens:
            if tok in operations:
                # we are dealing with an operator
                second = cur_elements.pop()
                first = cur_elements.pop()
                result = None

                if tok == "+":
                    result = first + second
                elif tok == "-":
                    result = first - second
                elif tok == "*":
                    result = first * second
                elif tok == "/":
                    # need to make it truncates towards zero
                    result = int(first/second)

                cur_elements.append(result)
            else:
                # we are dealing with an operand
                cur_elements.append(int(tok))

        return cur_elements[0]  

