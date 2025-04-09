from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_hash_map = {}

        for num in nums:
            if num in duplicate_hash_map:
                return True
            else:
                duplicate_hash_map[num] = num

        return False
