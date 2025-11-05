# KMP algorithm 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #
        #   KMP algorithm
        #   O(m + n) time complexity, O(m) space complexity
        #

        # build the lps table
        # O(m) time, O(m) space
        def build_lps(target):
            lps = [0] * len(target)
            for i in range(1,len(lps)):
                best = lps[i - 1]
                # we have not found a valid match and there are still more prefixes that could possible match to explore
                while best and target[i] != target[best]:
                    best = lps[best - 1]
                
                # see if we found a match
                if target[i] == target[best]:
                    best += 1
                
                lps[i] = best

            return lps

        # O(n) time
        def kmp(search, target):
            lps = build_lps(target)

            matches = 0
            for i in range(len(search)):
                # find the next longest possible amount of matches we could have
                while matches > 0 and search[i] != target[matches]:
                    matches = lps[matches - 1]

                # make sure we actually found a match
                if search[i] == target[matches]:
                    matches += 1
                
                # see if we fully matched the target string
                if matches == len(target):
                    return i - matches + 1
            
            return -1


        return kmp(haystack, needle)


        