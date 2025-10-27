from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # 
        # time[i] + time[j] = 60*k - time , 
        # (time[i]  % 60 + time[j] % 60 ) % 60 = 0
        # (time[i]  % 60 + time[j] % 60 ) = 60 * k
        # (time[i]  % 60 + time[j] % 60 ) = 60 or 0
        #
        #  Case 0: (time[i] % 60 + time[j] % 60) = 0 ==> time[i] % 60 = time[j] % 60 = 0
        #  Case 60: (time[i]  % 60 + time[j] % 60 ) = 60  ==> time[j]  % 60 = 60 - time[i] % 60 
        complement_freq = defaultdict(int)
        res = 0

        # common tactic to avoid double counting is to only register the complement as we process the value,
        # this way, we avoid counting the current value itself
        for num in time:
            val = num % 60
            complement = 60 - val
            
            # case 0
            if val == 0:
                res += complement_freq[0]
            else:
                # case 60
                res += complement_freq[complement]

            complement_freq[val] += 1
            
        return res

        