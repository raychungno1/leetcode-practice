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

        return s[maxStart: maxEnd + 1]

    def genPalindrome(self, s, l, r):
        # Move pointers outwards to find longest palindrome
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break

            l -= 1
            r += 1

        return (l + 1, r - 1)
