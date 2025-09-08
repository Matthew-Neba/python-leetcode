from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        Key to this problem is realzing the most frequent task is the bottle neck.
        If we know it, we can create blocks of length >= n that include that most frequent 
        task once and all the other tasks in the block (maximum block size of 26 since there
        are at most 26 unique tasks) . 
        O(n) time, O(n) space
        """
    
        count = Counter(tasks)

        most_frequent = max(count.values())
        amount_most_frequent = sum([1 for val in count.values() if val == most_frequent])

        main_blocks = (most_frequent - 1)*(n+1)
        end_block = amount_most_frequent

        return max(len(tasks), main_blocks + end_block)
