class Solution:
    def numDecodings(self, s: str) -> int:
        # 
        # For this problem, we realize that we can only maximally process the two digits
        # since the maximum value for the mapping is 26. Therefore, we can do dp as follows
        # 
        # If we can decode one character, decode it and get the number of ways to decode the rest of the string
        # If we can decode two characters, decode them and get the number of ways to decode the rest of the string
        # The number of ways to decode the current string we are considering will be the sum of them
        #
        # O(n) time complexity, O(n) space --> Can be space optimized with tabulation to O(1) space
        #
        def valid_mapping(s):
            # if leading zeros, invalid
            return s[0] != "0" and int(s) <= 26

        if len(s) == 1:
            return 1 if valid_mapping(s) else 0

        dp_old = 1 if valid_mapping(s[len(s) - 1]) else 0
        dp_older = 1

        for i in range(len(s) - 2, -1, -1):
            cur_decode = 0
            # decode one character
            if valid_mapping(s[i]):
                print(s[i])
                cur_decode += dp_old
            
            # decode two characters:
            if valid_mapping(s[i:i+2]):
                print(s[i:i+2])
                cur_decode += dp_older
            
            dp_older = dp_old
            dp_old = cur_decode
        
        return dp_old


