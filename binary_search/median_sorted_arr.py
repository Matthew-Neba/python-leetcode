from typing import List

# Key in this problem is realizng that we can always exchange problems for equivalent problems. This can potentially improve time and space complexity. They key to this problem was exchanging the problem of finding the exact median into a problem of partitioning both arrays into lower and high splits such that the lower split has half of the total values and the higher split has half of the total values. The median is then trivial to calculate from these partitions. This can be done in O(log(min(m,n))) time.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # choose minimum of both arrays to minimize time complexity to O(log(min(m,n)))
        choose_num = 1 if len(nums1) < len(nums2) else 2
        search_arr = nums1 if choose_num == 1 else nums2
        second_arr = nums2 if choose_num == 1 else nums1

        total_len = len(nums1) + len(nums2)
        half_elements = total_len // 2

        low, high = 0, len(search_arr)

        while high >= low:
            mid = (low + high) // 2
            elems_need = half_elements - mid

            # Partition values
            first_low_end = search_arr[mid - 1] if mid > 0 else float("-inf")
            first_high_start = search_arr[mid] if mid < len(search_arr) else float("inf")
            second_low_end = second_arr[elems_need - 1] if elems_need > 0 else float("-inf")
            second_high_start = second_arr[elems_need] if elems_need < len(second_arr) else float("inf")

            # Valid partition found
            if first_low_end <= second_high_start and second_low_end <= first_high_start:
                if total_len % 2 == 0:
                    return (max(first_low_end, second_low_end) + min(first_high_start, second_high_start)) / 2
                else:
                    return min(first_high_start, second_high_start)

            # Binary search adjustment
            elif first_low_end > second_high_start:
                high = mid - 1
            else:
                low = mid + 1
