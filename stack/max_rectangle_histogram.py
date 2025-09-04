from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #
        #
        # Can easily derive a O(n*m) time solution where m is the max bar height. We can easily
        # optimzie it to O(n^2) by only considering the bars we have in the array. However,
        # is there an O(n) time solution?
        #
        # The key insight to this problem is realizng that a lower height rectangle
        # can always use a heigher height bar to increase it's area. Can thus use a monotonic stack
        # for this problem.
        #
        # Other key insight is to avoid double counting bars. This can be done by never
        # modyfying bars already on the stack, instead just account for this while pushing elements unto the stack.
        # 
        # Suppose we are processing the bars from left to right.
        # We notice that if we encounter a greater bar height that we have encountered,
        # we would only like to change our current bar height if in the future,
        # we would end up with a greater area. But notice that once we decide to increase
        # our bar height, we could still use those higher bars by the previous lower bar rectangles.
        # Therefore, if we just maintain the count of the heigher bars, any rectangle at
        # a bar lower than it can use it to expand it's area. Easy to handle this if
        # bars are always increasing in height or remainiing the same. However, what if we
        # get a bar with a lower height while going from left to right? Well, we notice
        # That the previous higher bar cannot continue expanding it's area. So we can
        # pop it from the stack and add it's count to the bar right below it. 
        # We can keep repeating this popping process until we have a bar equal to or lower 
        # than our current processing bar. Since we are only adding and popping each bar from the 
        # stack once, it is O(n) time and O(n) space.
        # 

        stack = []
        res = float("-inf")

        for height in heights:
            # backwards width will store the width of rectangles >= height
            # that were popped off the stack
            backwards_width = 0

            # here, stack[-1] > height, we need to pop all the lower height
            # rectangles from the stack since we can no longer expand them
            while stack and stack[-1][0] >= height:
                cur_height, cur_count = stack.pop()

                # see if the current rectangle has the max area
                res = max(res, cur_height * (cur_count + backwards_width))

                backwards_width += cur_count

            
            stack.append([height, backwards_width + 1])

        # process the rest of the stack and compare to max
        backwards_width = 0
        while stack:
            cur_height, cur_count = stack.pop()

            # see if the current rectangle has the max area
            res = max(res, cur_height  * (cur_count + backwards_width))

            backwards_width += cur_count

        return res










