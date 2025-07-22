from typing import List

# Key this problem is realizing that if we know we can't reach the end of the array from the current position, then the next best choice is to pick the position we can jump to that allows us to go potentially go further than all the other possible jump positions.

# first solution. O(n) time complexity, O(1) space complexity. But a little long to code, can simplify.
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cur_index = 0
        jumps = 0

        if len(nums) == 1:
            return 0

        # check if we are at the end position
        while cur_index < len(nums) - 1:
            jump_power = nums[cur_index]

            # check if we can get to the end by using this jump
            if cur_index + jump_power >= len(nums) - 1:
                return jumps + 1

            # else, choose the largest possible jump we have acess to from this position
            choice_index = cur_index 
            furthest_loc = cur_index
            for jump in range(1,jump_power+1):
                jump_location = cur_index + jump + nums[cur_index + jump]
                if jump_location > furthest_loc:
                    furthest_loc = jump_location
                    choice_index = cur_index + jump

            cur_index = choice_index
            jumps += 1

# Same time and space complexity as the first solution, but eliminates the for loop by keeping track of the maximum position we can reach given the i'th as so far encountered in the array. Essentially, keep track of the current interval that the i'th jump has acess to and use max jump in the current interval to form the next interval. Can be done with two pointers.
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end_jump = 0
        furthest_position = 0

        for i in range(len(nums) - 1):
            furthest_position = max(furthest_position, i + nums[i])

            # check if we have reached the maximum position we can jump to from the previous jump
            if i == end_jump:
                # update the new maximum jump position
                end_jump = furthest_position
                jumps += 1

        return jumps

        

       

