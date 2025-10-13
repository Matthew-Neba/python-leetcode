from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # A variation of a monotonic stack where the stack update is based not only 
        # on 1) one condition (monoticity) but also on a second condition , 
        # 2) the validity of the collision
        #
        # Easier to view this problem as just a regular stack problem where we store valid candidate
        # collision cars. We use a stack to ensure we are always checking the nearest car to
        # the current car first.

        N = len(cars)
        stack = []
        res = [-1] * N

        for idx in range(len(cars) - 1, -1,-1):
            pos,speed = cars[idx]
            while stack:
                old_pos, old_speed, old_idx = stack[-1]

                # see if we collide with this car
                if old_speed >= speed:
                    stack.pop()
                    continue

                # check if we collide with the car this collided with (if so we dont collide with this car)
                collision_time = (old_pos - pos) / (speed - old_speed)
                if res[old_idx] > 0 and collision_time >= res[old_idx]:
                    stack.pop()
                    continue
                
                # we are at the valid collision car
                res[idx] = collision_time
                break

            stack.append((pos, speed, idx))
        return res


        

    