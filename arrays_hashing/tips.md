
### Tips:
-Key point about using hash sets/ hash maps is to cut down on excessive for loops. Since hash maps allow constant time lookup and edits, can completely eliminate some for loops. Useful for searching for properties/conditions on elements.

-Dictionaries in python also hold a seperate array for all the keys in the Hash Table, so iteration over all keys/values occur in O(n) time, where n is the number of keys inserted into the Dictionary

- Key to this top-k-frequent is realizing we can use Bucket Sort/Counting sort to sort elements according to thier frequency in O(n) time. Whenever we want to sort non negative numbers in a small bounded range, think of Bucket/Counting Sort variations

-Always see how to reuse/use previous computations to facilitate the current ones (ex: products of array except self)