class Solution:
    # Using multiplication and division seems tricky for this problem.
    # Can we use bit manipulation instead?
    #
    # Important to check constraints for bit manipulation problems to determine how many bits
    # to use and if we need to account for negative numbers and two's complement.
    #
    # Note that two's complement allows us to add negative and positive numbers the same.
    # No need to modify the logic. We just need to ignore the overflow that goes beyond
    # our bit system  (32 in this case). We can do this case by ignoring the last carry. 
    # Also need to know in python, this rule of two's complement holds: ~x + 1 = -x. However,
    # at the end, we need to convert the number to python's version of two's complement
    # with the infinite preceeding one's instead of just the MSB. This is due to the unbounded
    # size integers python has.
    # 
    def getSum(self, a: int, b: int) -> int:
        # need to similate the process of adding and carrying starting from the lowest bit
        res = 0
        non_carry = 0
        carry = 0

        max_positive_int = 0x7FFFFFFF

        for i in range(32):
            # extract the lowest bit
            a_lowest = (a >> i) & 1
            b_lowest = (b >> i) & 1

            # adder logic here
            # sum bit (non_carry)
            non_carry = a_lowest ^ b_lowest ^ carry

            # new carry
            carry = (a_lowest & b_lowest) | (carry & (a_lowest ^ b_lowest))
           
            # insert non_carry into the proper position
            res |= non_carry << i
        
        # handle negative values, in python, instead of the MSB being set in two's complement,
        # there is an infinite preceeding chain of ones.
        if res > max_positive_int:
            # Set all the bits ahead of the 31 bit to 1, python's version of two's complement
            res = ~(res ^ 0xFFFFFFFF)
           
        return res
