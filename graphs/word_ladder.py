from typing import List
from collections import deque


# We can optimize the below solution by realizing that from each word, we only need to check if we can reach any one letter mutation in our available words set. This means we need to compare the current word to 26 X m words instead of n words. i.e: Problem inversion once again. Instead of checking if the current word is different by at most 1 character from all the n words. Can check if any of the one character differences of the current word belongs in the n words. 
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # create a set to store the words
        available_words = set(wordList)
        queue = deque([beginWord])

        steps = 1
        while queue:
            steps += 1
            for _ in range(len(queue)):
                # process a word
                cur_word = queue.popleft()
                # Create 26 * M possible one character mutations of the current word and check
                # if any of them are available
                # O(26 * M * M) ---> extra M for copying the string
                for i in range(len(cur_word)):
                    for c_int in range(ord("a") , ord("z") + 1):

                        
                        new_word = cur_word[0:i] + chr(c_int) + cur_word[i+1:]
                       
                        # check if the word belongs in the available list
                        if new_word in available_words:

                            # check if the word is the target
                            if new_word == endWord:
                                return steps

                            # add it to queue and remove from available words
                            available_words.remove(new_word)
                            queue.append(new_word)
        
        return 0




# Key to this problem is realizing that the naive backtracking approach can be optimized. This is because we don't care of the exact path we take to get to a word, or the number of ways to get to it, etc. We only care if it is reachable within i steps. Therefore, if we can reach a word from some level in the backttracking tree, never consider the word for the other backtracking nodes in the same level or in any future level. Note that this problem now resemble a simple bfs.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # O(m) time complexity, O(1) space, couldh'v been O(1) if all we cared about was the frequencies
        # of the characters (compares 26 alphabet positions each time)
        def one_diff(first, second):
            diff = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    diff += 1
                if diff > 1:
                    return False
            return True

        
        # create a set to store the words
        available_words = set(wordList)
        queue = deque([beginWord])

        steps = 1
        while queue:
            steps += 1
            for _ in range(len(queue)):
                # process a word
                cur_word = queue.popleft()
                for new_word in list(available_words):
                    # check if we can reach the new word
                    if one_diff(cur_word, new_word):
                        # check if the word is the target
                        print(cur_word, new_word)
                        if new_word == endWord:
                            return steps

                        # never consider this word again
                        available_words.remove(new_word)
                        
                        # add it to queue
                        queue.append(new_word)
        
        return 0


