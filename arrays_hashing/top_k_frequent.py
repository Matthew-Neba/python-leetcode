
# Key to this problem is realizing we can use Bucket Sort/Counting sort to sort elements according to thier frequency in O(n) time. Whenever we have non negative numbers in a small bounded range, think of Bucket/Counting Sort variations

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num,0)
        
        # time for bucket sort variation (Variation: no internal sorting in the buckets to yield an O(n) solution)
        num_buckets = len(nums) + 1
        bucket_arr = [[] for i in range(num_buckets)]

        for num,freq in freq_dict.items():
            bucket_arr[freq].append(num)
        
        k_freq = []
        
        for i in range(num_buckets-1, 0, -1):
            for num in bucket_arr[i]:
                k_freq.append(num)

                if (len(k_freq) == k):
                    return k_freq

        



