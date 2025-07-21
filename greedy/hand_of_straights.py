from typing import List
from collections import Counter

# Key to this problem is beginning with the intuition that starting with the smallest value in the hand will allow us to build the longest possible sequence and thus, we should consider doing so. The question is then, why should we not use the smallest number in the hand? The answer is if using that smallest number will prevent us from building an additional sequence. Than can be done in two ways. 1) That smallest number is used in a higher sequence 2) That smallest number is used in a lower sequence. If it can be used in a higher sequence, then is must be our current sequence we are building since sequences are only buildable in one way(consetive by one), thus can eliminate case 2). For case 1), we note that since our current value is the smallest in the hand, it cannot be used to build a lower sequence. Thus case 1) and case 2) are eliminated. Our method will never impede the creation of another sequence while ensuring we properly build the sequences if possible. 

# Now can use a min-heap to consecutively get the minimum number available in our hand. However, repetitively doing this will give a time complexity of nlog(n). Instead of fetching the min, we can instead check if any given card is the start of a sequence. If not, keep decrementing the value and checking if that decremented value is the start of a sequence. Repeat until we get to a minimum then build the sequence up until it is no longer possible. The time complexity of this method is O(n) since each value is visited at most twice in the main work loop. potentially once when discovering the minimum value of the sequence it belongs to. The second time will be when building up the sequence it belongs to.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # count the cards   
        cards_count = Counter(hand)

        for card in hand:
            min_card = card

            # find the minimum card
            while cards_count[min_card - 1]:
                min_card = min_card - 1

            # build up the sequence, picking the minimum card encountered so far as the starting point. Repeat the process until we have iterated over every card we iterated over while getting the minimum of the sequence, necessary for the time complexity of O(n)
            build_up_card = min_card 
            while build_up_card <= card:
                while cards_count[build_up_card]:
                    for cur_card in range(build_up_card,build_up_card + groupSize):
                        if cards_count[cur_card] > 0:
                            cards_count[cur_card] -= 1
                        else:
                            return False

                build_up_card += 1
        return True
