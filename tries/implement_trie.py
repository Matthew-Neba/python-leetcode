
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class PrefixTree:
    """
    The main benefit of using a Trie over a hashmap is when we are 
    searching for the number of strings which have a certain prefix. 
    The time complexity for this operation would be O(p + k) where p
    is the length of the prefix and k is the number of string in the trie
    with the given prefix. For a hashmap, it would be O(n * p), since we 
    would have to check every string in the hashmap.
    
    Tries also allow more efficient storage of strings which share common
    prefixes in practice. This is is because all the prefixes will
    only be stored once in the trie.

    1) A TrieNode should have 
        1) a children dict mapping characters to child nodes 
        2) A marker denoting whether a word ends at this node
        
    2) Use for loops in all the tries operations. Makes the code cleaner

    """
    def __init__(self):
        self.head = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                new_node = TrieNode()
                cur.children[ch] = new_node

            cur = cur.children[ch]
        
        cur.end_word = True

    def search(self, word: str) -> bool:

        cur = self.head
        for ch in word:
            if ch not in cur.children:
                return False
  
            cur = cur.children[ch]
            
        return cur.end_word


    def startsWith(self, prefix: str) -> bool:

        cur = self.head
        for ch in prefix:
            if ch not in cur.children:
                return False
  
            cur = cur.children[ch]
            
        return True


        
        