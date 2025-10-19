from typing import List
import random

class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:

        # preprocess to generate all necessary matches
        total_matches = []
        for i in range(n):
            for j in range(i+1,n):
                total_matches.append([i,j])
                total_matches.append([j,i])
        
        # greedy randomization now
        for _ in range(3000):
            res = []
            matches = [m[:] for m in total_matches]
            random.shuffle(matches)

            # try and assign matches for every day
            for _ in range(len(total_matches)):
                found = False
                # try and find the first valid match
                for i in range(len(matches)):
                    team1, team2 = matches[i]
                    if res and (team1 in res[-1] or team2 in res[-1]):
                        continue
                    else:
                        res.append(matches[i])
                        matches[i], matches[-1] = matches[-1], matches[i]
                        matches.pop()
                        found = True
                        break
                
                if not found:
                    break
            
            if len(res) == len(total_matches):
                return res
        
        # probability of getting here without finding a match for valid n is quite low,
        # n is probably not valid
        return []

                







