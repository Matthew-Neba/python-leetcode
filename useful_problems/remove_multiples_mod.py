class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        #
        # When dealing with modular equations, try and use the modular relationships to our advantage to cancel out 
        # multiples of the modular term when possible. ex: for this problem, we can always remove multiples of k
        # from iteration to iteration.
        #
        # We can use this to our advantage since we are performing the same *10 + 1 and thus, if we get to the same cur value,
        # we have a cycle and cannot find some integer of all ones divisible by k.
        #  
        cur = 1
        length = 1
        seen = set()
        while cur not in seen:
            if cur % k == 0:
                return length

            # add to set
            seen.add(cur)
            
            # shift positions of previous ones
            cur *= 10
            # add contribution of this one
            cur += 1

            # reduce cur to remainder
            cur %= k

            # increase length
            length += 1
        
        return -1
        