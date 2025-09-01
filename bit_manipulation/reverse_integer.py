import math
class Solution:
    def reverse(self, x: int) -> int:
        #
        # Key issue is that we are storing the numbers in binary so when we shift them,
        # it is changing them by powers of 2 instead of powers of 10. Need to fix this.
        # 
        # Can use math.fmod here
        # reverse the digits
        #
        #   Remeber can use % and // to extract digits in a non binary system. For binary
        # can just use shifts and masks. 
        #
        # Always use math.fmod() if doing modulo in python

        min_val = -(2**31)
        max_val = 2**31 - 1

        res = 0

        while x != 0:
            # careful with mod and negative values in python, -1 % 10 = 9
            # math.fmod(-1,10) == -1. fmod preserves sign of the dividend.
            digit = math.fmod(x,10)

            # careful with // in  python --> -1//10 = -1
            x = int(x/10)

            # check overflow without going using too many bits, problem inversion. instead of checking (res * 10) + digit < max_value, we can instead check res > (max_val - digit) / 10. This will allows us to not use excess bits.
            if res > (max_val - digit) / 10:
                return 0
            
            if res < (min_val - digit) / 10:
                return 0
            
            res = (res * 10) + digit
        
        return res

