### Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.

---

<details>
<summary><b>Brute Force</b></summary>
  
The initial idea is to check every possible substring of `s`, returning the length of the longest substring that is a palindrome. 

*Time: `O(n^3)`*
>Iterating through each substring is `O(n^2)`, but we also have to check valid palindromes, which is an `O(n)` operation. 

*Space: `O(1)`*
> No special data needs to be stored.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStart = 0
        maxEnd = 0

        # Iterate through each substring
        for l in range(len(s)):
            for r in range(l, len(s)):

                # If substring has is a palindrome, 
                # update the result
                if self.isPalindrome(s, l, r) and (r - l) > (maxEnd - maxStart):
                    maxStart = l
                    maxEnd = r
        
        return s[maxStart : maxEnd + 1]

    def isPalindrome(self, s, l, r):
        # Move pointers inwards to check for palindrome
        while l < r:
            if s[l] != s[r]: return False

            l += 1
            r -= 1

        return True
```
</details>

---
<details>
<summary><b>Hint for Optimal Solution</b></summary>
  
Try to find the palindrome "centered" at each character. Note that palindromes have both even & odd cases. 

</details>

---
<details>
<summary><b>Optimal</b></summary>

Iterate through each character in the string. At each character, find the longest even-length and odd-length substring centered at this character. 

*Time: `O(n^2)`*
>Iterating through the string is `O(n)` and generating the long palindrome is `O(n)`.

*Space: `O(1)`*
> No special data needs to be stored.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStart = 0
        maxEnd = 0

        # Iterate through character
        for i in range(len(s)):

            # Odd length palindrome
            l, r = self.genPalindrome(s, i, i)
            
            # Update longest substring
            if (r - l) > (maxEnd - maxStart):
                maxStart = l
                maxEnd = r

            # Even length palindrome
            l, r = self.genPalindrome(s, i, i + 1)

            # Update longest substring
            if (r - l) > (maxEnd - maxStart):
                maxStart = l
                maxEnd = r
        
        return s[maxStart : maxEnd + 1]

    def genPalindrome(self, s, l, r):
        # Move pointers outwards to find longest palindrome
        while l >= 0 and r < len(s):
            if s[l] != s[r]: break

            l -= 1
            r += 1

        return (l + 1, r - 1)
```

---