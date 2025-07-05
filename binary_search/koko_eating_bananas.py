from typing import List

# Key to this problem was realizing that there is a more genral form of binary search. I call this "biinary elimination". Binary elimination is just a process for eliminating half of the search space by performing a series of checks in constant time. Any algorithm like binary search which follows this pattern can reduce the search space to one value in O(logn) time. The specific check for this problem was checking if koko can eat all the bananas with the given k/hour rate.

# Note that for this problem. It is not necessary to create a duplicate array which we will search the values for valid k. We just need store the indexes. This is because we already know the value of the index without doing arr[index] due to the strictly ascending by 1 structure of the search array. ex: [1,2,3,4]

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #function to check if bananas can be eaten in at rate k within hours h, O(n)
        def check_eat(piles,k,h):
            hours_eaten = 0
            for pile in piles:
                hours_eaten += pile // k
                hours_eaten += (1 if (pile % k) > 0 else 0)

            if hours_eaten <= h:
                return True
            else:
                return False
        
        # now just check if bananas can be eaten at current value in search array, 
        # eliminating half the values based on the result of that check, n * log(m)

        # note, don't need this search arr since we already know that the array is ordered in ascending order by 1,
        # don't need to keep track of indexes in this implementation of binary search
        # since we already know elements at each index , [1,2,3,4], at index 2 we have 2.
        
        # search_arr = [i for i in range(1,max_pile+1)]
        low, high = 0, max(piles) - 1
        while high >= low:
            mid = (high + low) // 2

            # Since we are not updating the low and highs with mid + 1 and mid - 1 respectively, (using mid) low and high will not converge to same index. They will be one apart by one, Can check this convergence  then by using high - low == 1
            if check_eat(piles,mid+1,h):
                if high - low == 1:
                    return low+1
                else:
                    high = mid
            else:
                if high - low == 1:
                    return high + 1
                else:
                    low = mid
                










