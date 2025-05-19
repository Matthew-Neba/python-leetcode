- Sliding window is often involved when we are searching for contiguos elements/sub-strings/sub-sequences that match a certain condition. Often need to maintain some aggregate (frequency,sum,product,etc.) of the elements in the window

-Key to sliding window properties is assuring that the sliding window has an invariant property (some condition that is always met). This can be no duplicates, maximum number of replacements, etc. Then use this sliding window to simplify some brute force search to be in linear time

-When using while loop to implement sliding window, may sometimes need to do one final phase of shrinking the left pointer for the final index of the right pointer. Could be avoided if sliding window was implemented with a for loop for every possible right pointer position
