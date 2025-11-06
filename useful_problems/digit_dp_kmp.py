class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        
        def build_lps(goal):
            lps = [0] * len(goal)

            for i in range(1, len(goal)):
                best = lps[i - 1]

                while best > 0 and goal[i] != goal[best]:
                    best = lps[best - 1]

                if goal[i] == goal[best]:
                    best += 1
                
                lps[i] = best

            return lps

        lps = build_lps(evil)
        dp = {}
        def good_strings(pos, evil_done, greater_s1, less_s2):
            if (pos, evil_done, greater_s1, less_s2) in dp:
                return dp[(pos, evil_done, greater_s1, less_s2)]
            
            # base case, no chars left to pick
            if pos == n:
                return 1

            res = 0

            lower_bound = ord(s1[pos]) if not greater_s1 else ord("a")
            upper_bound = ord(s2[pos]) if not less_s2 else ord("z")

            for c_val in range(lower_bound, upper_bound+1):
                c = chr(c_val)

                new_evil_done = evil_done

                # now use kmp to figure out the next longest match
                while new_evil_done > 0 and c != evil[new_evil_done]:
                    new_evil_done = lps[new_evil_done - 1] 

                # see if we found a match
                if c == evil[new_evil_done]:
                    new_evil_done += 1
                
                # terminate if we matched the whole evil string
                if new_evil_done == len(evil):
                    continue
                
                # get new bounds
                new_greater_s1 = greater_s1 if greater_s1 else c > s1[pos]
                new_less_s2 = less_s2 if less_s2 else c < s2[pos]

                # add to res
                res += good_strings(pos + 1, new_evil_done, new_greater_s1, new_less_s2) % MOD
            
            dp[(pos, evil_done, greater_s1, less_s2)] = res % MOD
            return dp[(pos, evil_done, greater_s1, less_s2)]

        return good_strings(0, 0, False, False) % MOD
