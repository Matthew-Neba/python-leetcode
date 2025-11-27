from sortedcontainers import SortedList, SortedSet
from collections import defaultdict
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        #
        # If we cannot get away with lazy deletions with a heap, time to consider using a balanced BST 
        # (SortedList or SortedSet).
        # Usually happens when we want to snipe heap values to edit them but would cost O(n) in a heap.
        #
        # SortedList + Dict is a solution to this. We can use the Dict to assist in finding values in the SortedList
        #
        # - Remove the old (freq, item) pair of the old sliding window element from sortedlist using global freq table if there
        # - Decrement it from global dict
        # - Insert element into bst using (new freq, elem) as key if was there before
        # = Adjust top x sum if key was there before
        #
        # - Remove the old (freq,item) pair from sortedlist using global freq table if there
        # - Increment the freq count in the global dict
        #
        # - Insert element into bst using (new freq, elem) as key if there, adjsut top x sum if key was there
        # - If was not there, add it but will have to remove the min freq item. Adjsut eh top x sum accordingly
        #
        top_x_sum = 0
        freq = defaultdict(lambda: 0)
        top_x = SortedList()
        rest = SortedList()

        # add element to the sliding window
        def add(elem):
            nonlocal top_x_sum
            old_freq = freq[elem]
            # elem was in top x, it stays there
            if old_freq > 0:
                if (old_freq, elem) in top_x:
                    top_x.remove((old_freq, elem)) 
                    top_x_sum -= old_freq * elem
                else:
                    rest.remove((old_freq, elem)) 
                
            # update freq
            freq[elem] = old_freq + 1

            # move updated value into rest so that reorder can get the next highest frequency
            rest.add((old_freq + 1, elem))
            reorder_top_x()
            
        def remove(elem):
            nonlocal top_x_sum
            old_freq = freq[elem]

            # elem was in top x
            if (old_freq, elem) in top_x:
                top_x.remove((old_freq, elem)) 
                top_x_sum -= old_freq * elem
            else:
                # element was not in top_x
                rest.remove((old_freq, elem))

            # update freq
            freq[elem] = old_freq - 1
            if freq[elem] > 0:
                rest.add((freq[elem], elem))

            reorder_top_x()
        
        # this function makes sure that top_x has the top x elements after an update, replaces the min if necessary
        def reorder_top_x():
            nonlocal top_x_sum
            # see if top_x is not full
            if len(top_x) < x and rest:
                # get the max item from rest
                add_top_x = rest.pop(-1)
                top_x.add(add_top_x)
                top_x_sum += add_top_x[0] * add_top_x[1]
            elif len(top_x) == x and rest:
                # see if we need to replace an element from top_x
                min_top_x = top_x[0]
                # replace element (greedily use the highest item in rest)
                if rest[-1] > min_top_x:
                    top_x_sum -= min_top_x[0] * min_top_x[1]
                    top_x_sum += rest[-1][0] * rest[-1][1]
                    top_x.remove(min_top_x)
                    top_x.add(rest[-1])
                    rest.remove(rest[-1])
                    rest.add(min_top_x)

        # Initialize the first window
        for i in range(k):
            add(nums[i])
        
        result = [top_x_sum]
        
        # Slide the window
        for i in range(k, len(nums)):
            # Remove the leftmost element of the window
            remove(nums[i - k])
            # Add the new rightmost element
            add(nums[i])
            result.append(top_x_sum)
        
        return result
