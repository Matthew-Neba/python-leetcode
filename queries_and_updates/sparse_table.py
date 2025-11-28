
"""
Sparse table is for efficiently handling range queries with operations that:

1) Can be broken down into the same operation over a smaller range
2) Don't care if we break down the range into non disjoint segments

# ex: min([0 ,11]) = min(min([0, 5]) , min([5, 11])) 
# notice that condition 2 holds since min([0, 11]) = min(min([0,5]), min([2, 11]))   ([0,5] and [2,11] have elements in common so they are not disjoint)

Sparse table does not support updates.

Big idea is to get all subarrays of length equal to a power of 2 and compute the operation over those subarrays. We can then use that precomputation to answer all range queries. There are nlogn of these subarrays, and the computation of the operation over the subarray uses the previous subarrays answers to do them in O(1) time. O(nlogn) time and O(nlogn) space for building sparse table. 

After precomputation, we answer the range queries in O(1) time by taking the biggest power of 2 that fits into the query range, getting the answer for it, and then offsetting that subarray to cover the elements that were missed. We then combine those two operations by taking advantage of the fact that the operation doesn't care that the segments are not disjoint.
"""

# Implementation of a Sparse Table using Max operation
# O(nlogn) time, O (nlogn) space to build
# O(1) query
import math
class MaxSparseTable:
    def __init__(self, arr):
        N = len(arr)

        levels = int(math.log(N , 2)) + 1

        # build the sparse table
        self.table = [[0]*N for _ in range(levels)]

        # base case handle lengths of 1
        for i in range(N):
            self.table[0][i] = arr[i]

        # handle all sizes
        for power_of_2 in range(1,levels):
            size = 1 << power_of_2
            pos = 0
            while pos + size - 1 < N:
                offset = size >> 1
                self.table[power_of_2][pos] = max(self.table[power_of_2 - 1][pos], self.table[power_of_2 - 1][pos + offset])
                pos += 1
    
    def query(self, low, high):
        length = high - low + 1

        # find greatest power of two to fit in interval
        max_size = int(math.log(length, 2))

        return max(self.table[max_size][low],self.table[max_size][high - (1 << max_size) + 1])






