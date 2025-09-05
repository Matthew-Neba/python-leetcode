from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #
        #
        # Is sorting necessary? Yes, any car is limited by the car ahead of it
        #
        # Key insight to this problem is realizing that if a car arrives later than the car aehad of it, a new fleet must be created. However, if it is has an earlier or equal arrival time, it is in the same fleet as that car. Note that fleet speeds are also determined by the first car in a fleet since no car behind it can pass it.
        
        fleets = 0

        sorted_pairs = sorted(zip(position,speed))
        prev_car_arrival = float("-inf")
    
        # process cars starting from the end
        for position,speed in reversed(sorted_pairs):
            # calculate current car arrival time
            rem = target - position
            # we need precise arrival times for this question, use floats instead of math.ceil(/)
            cur_arrival_time = rem/speed

            if cur_arrival_time > prev_car_arrival:
                # we cannot catch up to the next car, increase fleets
                fleets += 1
                prev_car_arrival = cur_arrival_time
            
        return fleets
                







