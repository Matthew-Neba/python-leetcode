from collections import defaultdict

# In this problem, we follow a binary search pattern: candidate optimization. We use binary search to fetch all possible candidates in logn time, and we compare the candidates to one another to ensure we have the optimal one. Used in binary elimination problems where we are not looking for an exact target element, but some element that matches some criteria.

class TimeMap:

    def __init__(self):
        self.kv_dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_dict[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        search_arr = self.kv_dict[key]

        low, high = 0 , len(search_arr) - 1

        recent = None
        while high >= low:
            
            mid = (high + low) // 2

            if timestamp == search_arr[mid][0]:
                return search_arr[mid][1]
            elif timestamp > search_arr[mid][0]:
                # Store value just beneath the mid value, this is the closest value in arr that is smaller than the timestamp. This is a possible candidate.
                recent = mid  # This is a candidate! Store it.
                low = mid + 1  # But keep searching for a better candidate
            else:
                high = mid - 1

        # important to use is not None, this is because the number 0 is also falsy in python
        if recent is not None:
            return search_arr[recent][1]
        else:
            return ""