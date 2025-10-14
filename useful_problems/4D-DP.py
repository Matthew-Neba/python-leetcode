from typing import List
import math
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        # Distinct numbers in the sequence are crucial for determinig if k condition is met
        #
        # Key to this problem is realizing that we can use DP to retrieve the sum of all the
        # smaller sequences needed for this sequence and thus, we will just need to multiply those
        # sums buy the current element we choose to include.
        #
        # 4D DP? Keep track of the carry to easily determine our current ones and the carry ones
        #
        #
        MOD = 10**9 + 7

        # compute pascals table for O(1) combinations calculation
        C = [[0] * (31) for _ in range(31)]
        for i in range(31):
            C[i][0] = C[i][i] = 1
            for j in range(1,i):
                C[i][j] = C[i-1][j-1] + C[i-1][j]

        dp = {}
        def find_products(choice_idx, seq_length, number_ones, carry):

            if (choice_idx, seq_length, number_ones, carry) in dp:
                return dp[(choice_idx, seq_length, number_ones, carry)]

            if choice_idx == len(nums):
                if seq_length != 0:
                    return 0
                
                # see how many ones the carry would generate, we need it to match the remaining ones
                if number_ones - bin(carry).count("1") == 0:
                    return 1
                else:
                    return 0
                
            sum_products = 0
            # take (any number of times), accounting for the combinations in the sequences
            for t in range(seq_length+1):
                # retrieve the ways to combine
                comb = C[seq_length][t]

                set_one = (carry + t) % 2
                new_carry = (carry + t)//2

                sum_products += (comb * pow(nums[choice_idx],t,MOD) * 
                find_products(choice_idx + 1, seq_length - t, number_ones - set_one, new_carry)) % MOD
            
            dp[(choice_idx, seq_length, number_ones, carry)] = sum_products
            return dp[(choice_idx, seq_length, number_ones, carry)]

        return find_products(0,m,k,0) % MOD
            

            

            




        