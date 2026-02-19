from itertools import groupby
from functools import cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        # 
        # can't seem to find a greedy solution. Consider dp.
        #
        # 3 Key Points for this problem:
        #
        # 1) Considering only the "last print" for each position gives us independent subproblems.
        #    Why? A print operation covers a contiguous range. So if a, b, and c are the last
        #    prints at their respective positions in: a [xyx] b [xyxy] c
        #    then no print operation responsible for a character inside [xyx] can extend past
        #    the boundaries set by a, b, or c. If it did, there are only two cases, both contradictions:
        #      - It happens AFTER the last print of a/b/c → it overwrites a/b/c, contradicting
        #        that a/b/c was the last print at that position.
        #      - It happens BEFORE the last print of a/b/c → a/b/c's print then overwrites it,
        #        contradicting that it was the last print for that character inside [xyx].
        #    This means the subproblems [xyx] and [xyxy] are fully contained and independent
        #    of each other and of a, b, c.
        #
        # 2) This allows us to reason about various combinations we can perform these last prints. We use 
        # a trick used in problems like combination sum to ensure we never have to look backwards as well
        # while handling all possible combinations, making the dp viable.
        # 
        # 3) We lazily handle the final print groupings, further simplifying the dp implementation.
        # 
        
        # simple, adjacent elements are essentially one element
        s = [ch for ch, _ in groupby(s)]

        @cache
        def printer(start, end):
            if start > end:
                return 0

            if start == end:
                return 1
            
            # consider the case where we don't choose to group the final print of this pos with the
            # final pring of any more positions
            best = 1 + printer(start + 1, end)

            # now, we can choose any number of future pos to the have thier final print grouped
            # with the final print of this char. Notice that for this to be possible though, 
            # the char at this pos has to match the char at future positions (s[start] == s[future_pos]).
            # Also (notice that we only need to consider future chars, 
            # no need to consider chars in previous positions. We have structured the dp so that 
            # all possible combinations of groupings of our char will be considered. 
            # (Similar to something like combination sum)).
            #
            # Another key step here is that instead of immediately grouping final prints
            # and adding 1 to total cost of printing, we can just ignore the current char 
            # and only handle cost of printing the other char. This way,
            # when we print the other char, all the chars that were grouped to it 
            # will be printed at the cost of that single char which will we 1.
            #
            for i in range(start + 1, end + 1):
                if s[start] == s[i]:
                    best = min(best, printer(start + 1, i - 1) + printer(i, end))
            return best

        return printer(0, len(s) - 1)


            


            
            