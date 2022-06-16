class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        d = set()  # HashSet of seen characters

        l = 0  # left & right pointers
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
