from typing import List

# Key to this problem is realizing that if we do no thave enough gas to complete a segment of the array, then every single station in that segment cannot be a valid solution. This is because, for every station in the current segment,  it can only gain gas from the previous stations in the segments or gain nothing at all. It cannot acquire negaive gas. Therefore, once a segment fails, we can safely skip all its stations and begin checking from the next station outside of the segment. Another key point is realizing that once we reach the end of the array, if the remaining gas is enough to cover the total gas shortfall encountered earlier, then, the starting station which allowed us to get to the end of the array is a valid solution.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = r = 0
        need_gas = 0
        current_gas = 0

        # see if we can get to the end of the array from some position
        while r < len(gas):
            current_gas += gas[r]

            if current_gas >= cost[r]:
                # continue the journey
                current_gas -= cost[r]
                r += 1
            else:
                # cannot continue the journey, reset gas tank, record needed gas
                need_gas += cost[r] - current_gas
                current_gas = 0
                r += 1
                l = r
        
        # check if when we get to the end of the array, we have enough left over gas to compensate
        # for all the missing gas we had while traversing the array
        return l if current_gas >= need_gas else -1