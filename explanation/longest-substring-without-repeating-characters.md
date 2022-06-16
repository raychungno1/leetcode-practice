### Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

---

<details>
  <summary><b>Brute Force</b></summary>
  
The initial idea is to check every possible substring of `s`, returning the length of the longest substring without repeating characters. 

*Time: `O(n^3)`*
>Iterating through each substring is `O(n^2)`, but we also have to check for repeat chars, which is an `O(n)` operation. 

*Space: `O(1)`*
> This may seem like `O(n)` due to the Hash Set, but since we're limited to Engligh letters & digits, the set takes `O(26 + 26 + 10)` space, which is constant.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        # Iterate through each substring
        for l in range(len(s)):
            for r in range(l, len(s)):

                # If string has all unique characters, 
                # update the result
                if self.noRepeat(s[l:r+1]):
                    maxLen = max(maxLen, r - l + 1)

        return maxLen

    def noRepeat(self, s):
        # Use dictionary to store visited chars
        charSet = set()

        for char in s:
            if char in charSet:
                return False
            charSet.add(char)

        return True
```
</details>

---
<details>
  <summary><b>Hint for Optimal Solution</b></summary>
  
Use a sliding window - if we see the same character twice, shrink the window.

</details>

---
<details>
  <summary><b>Optimal</b></summary>

A second approach is to use a sliding window, which is a two-pointer algorithm.

Start with both pointers, say a `left` and a `right` pointer, at the start of the string. Thus we have a string of length 1, which never has repeat chars. 

The idea is to expand the `right` pointer until this condition no longer holds, and a duplicate char is detected. 

Once this occurs, we then begin to shift the `left` pointer forwards until the condition holds again. 

*Time: `O(n)`*
>Each character is only checked once. Since HashSet lookups are constant, this will be linear. 

*Space: `O(1)`*
> Same as brute force solution.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        d = set() # HashSet of seen characters
        
        l = 0 # left & right pointers
        for r in range(len(s)):
            char = s[r]

            # While a duplicate char is found,
            # shift the left pointer until
            # there are no more duplicates
            while char in d:
                d.remove(s[l])
                l += 1

            # Add the character to our "seen" HashSet
            d.add(char)
            maxlen = max(maxlen, r - l + 1)
            
        return maxlen
```
</details>

---