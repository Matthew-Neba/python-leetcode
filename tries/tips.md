
TrieNode should have:
1. Children: A dictionary mapping characters to child nodes.
2. End-of-Word Marker: A boolean flag indicating whether a word ends at this node.

Trie Operations
-   Use for loops in all Trie operations (insert, search, startsWith).
-   This keeps the code cleaner and easier to read


- Tries are useful when dealing with string prefixes and wanting to do some cases of simple string pattern matching (cannot efiiciently deal with wildcards mapping to multiple characters)