from math import gcd
from typing import List
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 
        # a * x + b * y + ... + c * z = 1 , Immediately start thinking of Bezout's identiy and the Diophantine
        # Criterion
        # 
        #
        # Generalized Bezout's Identity: a * x + b * y + ... + c * z = gcd(x,y,z) always has a solution
        #
        # Diophantine criterion: a * x + b * y + ... + c * z = b iff gcd(x,y,...,z) | b
        #
        # This can easily be seen because gcd(x,y,...,z) | a * x + b * y + ... + c * z
        #
        # ax + by + cz = d , let d = gcd(x,y,z), trying to show a solution of that form exists
        #
        #
        # ax + by = gcd(x,y) (By base Bezout's identity)
        #
        # let gcd(x,y) = g1
        #
        #
        # gcd(g1, c) = gcd(gcd(a,b), c) = gcd(a,b,c)
        # let gcd(g1, c) = g2
        #
        # ug1 + vc = g2  (By base Bezout's identity) ==>
        # u(ax + by) + vc = g2 has a solution ==> lx + my + nz = gcd(x,y,z) , this inductive logic can be applied
        # to infinite variables.
        #
        # Notice that if the gcd of the whole array is greater than 1, then any pair or greater of elements will
        # also have a gcd of 2. So, the array must have a gcd of 1. If the gcd is 1, then we can use all the elements
        # as well to solve the equation by the generalized Bezout's identity.
        # 
        N = len(nums)

        # calculate the gcd of the whole array
        cur_gcd = nums[0]
        for i in range(1, N):
            cur_gcd = gcd(cur_gcd, nums[i])

        return cur_gcd == 1
        





        