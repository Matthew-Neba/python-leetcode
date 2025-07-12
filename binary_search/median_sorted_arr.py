from typing import List

# Key in this problem is realizng that we can always exchange problems for equivalent problems. This can potentially improve time and space complexity. They key to this problem was exchanging the problem of finding the exact median into a problem of partitioning both arrays into lower and high splits such that the lower split has half of the total values and the higher split has half of the total values. The median is then trivial to calculate from these partitions. This can be done in O(log(min(m,n))) time.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # TODO: ensure nums1 contains the minimum lenth array
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2, nums1

        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        # partitioning process using binary search
        # note, the indexes for low and high are different than regular binary search to handle special small array edge cases
        low , high = -1 , len(nums1) - 1
        while high >= low:
            mid = (high + low) // 2
            elems_needed = half_len - mid - 1

            # TODO: proper handling of the edge cases when the parition may include whole small arr or none of it
            nums1_low_end = nums1[mid] if mid > -1 else float("-inf")
            nums1_high_start = nums1[mid+1] if mid < len(nums1) - 1 else float("inf")

            nums2_low_end = nums2[elems_needed - 1] if elems_needed > 0 else float("-inf")
            nums2_high_start = nums2[elems_needed] if elems_needed < len(nums2) else float("inf")
            
            # TODO: verification of correct partitions, ensure using <= here important
            if nums1_low_end <= nums2_high_start and nums2_low_end <= nums1_high_start:
                if total_len % 2 == 0:
                    return (max(nums1_low_end, nums2_low_end) + min(nums1_high_start, nums2_high_start)) / 2
                else:
                    return min(nums1_high_start, nums2_high_start)

            elif (nums1_low_end > nums2_high_start):
                high = mid - 1
            else:
                low = mid + 1
