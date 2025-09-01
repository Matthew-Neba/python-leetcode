class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Shift and extract lower bit
        # Set it to corresponding bit in the front of the numer by adding the power of 2 to res
            
        for i in range(32):
            lower_bit = (n >> i) & 1
            # can also use | instead of + here for setting the bits
            res += lower_bit << (31 - i)
            
        return res
                  
                   