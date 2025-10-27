
class Solution:
    # An example of dp with prefix sums. If we have some type of linear dp recurrence relationship, we can sometimes use prefix sums to speed up the dp. If each dp uses the same amount of variables as well, we can use matrix exponentiation to speed it up as well. See zig zag arrays 2 for this.
    
    # O(2 * n * (r - l + 1)) time complexity , O(2 * n * (r - l + 1)) space complexity
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        
        vals = r - l + 1

        up_dp = [[0] * vals for _ in range(n)]
        down_dp = [[0] * vals for _ in range(n)]

        up_prefix = [0] * (vals + 1)
        down_prefix = [0] * (vals + 1)
        
        # base case
        for i in range(vals):
            up_dp[0][i] = 1
            down_dp[0][i] = 1
        
        # prefix base case
        for i in range(1, vals + 1):
            up_prefix[i] = (up_prefix[i - 1] + up_dp[0][i - 1]) % MOD
            down_prefix[i] = (down_prefix[i - 1] + down_dp[0][i - 1]) % MOD
        
        for i in range(1, n):
            for prev_val in range(vals):
                # update the up arr
                rec_sum = down_prefix[vals] - down_prefix[prev_val+1]
                up_dp[i][prev_val] = rec_sum % MOD

                # update the down arr
                rec_sum = (up_prefix[prev_val]) % MOD
                down_dp[i][prev_val] = rec_sum % MOD

            # update the prefix sum values
            for j in range(1, vals + 1):
                up_prefix[j] = (up_prefix[j - 1] + up_dp[i][j - 1]) % MOD
                down_prefix[j] = (down_prefix[j - 1] + down_dp[i][j - 1]) % MOD
            

        res = 0
        # for each val, can go up or down for the first value
        for i in range(r - l + 1):
            res += up_dp[-1][i] % MOD
            res += down_dp[-1][i] % MOD
        
        return res % MOD