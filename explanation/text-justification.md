### Text Justification

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

* A word is defined as a character sequence consisting of non-space characters only.
* Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
* The input array `words` contains at least one word.

---
<details>
<summary><b>Hint for Optimal Solution</b></summary>
  
Process the lines one at a time; trying to fit as many words into a line as possible knowing that there must be at least 1 space between words. 

Then try to split the remaining spaces between each word. 

</details>

---
<details>
<summary><b>Optimal</b></summary>

This solution utilizes a `buffer` queue. At its core, we fill up the buffer until `maxWidth` is reached, then calculate the spacing required to form each line. 

First initialize an output array to hold the resulting lines. 

Next, initialize the `buffer` queue to contain the first string of our input `words` array, and a `bLen` variable, initialized to the length of this first word. `bLen`  indicates the minimum possible length of the buffer. 

Now, loop through the array, adding words to the `buffer` queue until `bLen > maxWidth`. Note that `bLen` must be incremented by `1 + len(word)`, since there must be at least 1 space between words. 

Once adding a string results in exceeding `maxWidth`, its time to process our string. There are two cases:

1. If `len(buffer) == 1`, put this word at the start of the string, then pad spaces to fill our `maxWidth` requirement.

2. Otherwise, we can now calculate the number of spaces required to fill between each word. 

<table><tr><td>

Since `bLen` denotes the minimum width, we can find the # of spaces left to fill with `extra = maxWidth - bLen`.

These spaces will have to be divided evenly between the word gaps. The number of gaps that we need to divide is equal to `len(buffer) - 1`, so we can find this padding amount with:
 `spaceCount = extra // (len(buffer) - 1) + 1`.

 The `+1` is required since our `bLen` is already accounting for a single space between words. 

Furthermore, there may still be some spaces left over, which must be allocated to the gaps on the left. We can calculate how many of these gaps need extra spaces with:
 `extraSpace = extra % (len(buffer) - 1)`

</td></tr></table>

Once the required spacing is calculated, simply fill the first `extraSpace` gaps with `spaceCount + 1` number of spaces, then fill the rest of the gaps with `spaceCount` number of spaces. 

Once a line has been formed, append it to the output, initialize our `buffer` to the currently iterated word, and reset `bLen` to the length of this word. 

Finally, at the end of the loop there may still be remaining words in the buffer. Simply add a single space between these remaining words, then pad extra spaces to fill our `maxWidth` requirement.

*Time: `O(n)`*
>We are iterating through the input `words` array a twice - once to fill our buffer and a second time to empty our buffer and form our lines. 

*Space: `O(n * maxWidth)`*
> The worst case is when each word is on its own line, each of which has a mininum length of maxWidth. 

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buffer = [words[0]]
        bLen = len(words[0])
        out = []
        
        # Iterate through each word
        for i in range(1, len(words)):
            
            l = len(words[i])
            # If adding this word to the buffer results in bLen > maxWidth
            # its time to process a new line to our output
            if bLen + l + 1 > maxWidth:
                extra = maxWidth - bLen

                # If buffer length is 1
                if len(buffer) == 1:
                    out.append(buffer.pop(0) + " " * extra)
                    
                # Otherwise, calculate the space paddings necessary
                # then construct the line
                else:
                    spaceCount = extra // (len(buffer) - 1) + 1
                    extraSpace = extra % (len(buffer) - 1)

                    line = ""

                    while buffer:
                        line += buffer.pop(0)
                        if buffer:
                            line += " " * spaceCount
                            if extraSpace:
                                line += " "
                                extraSpace -= 1
                            
                    out.append(line)
                    
                bLen = l
            else:
                bLen += l + 1
                
            buffer.append(words[i])

        # Taking care of extra words in our buffer
        if buffer:
            out.append(" ".join(buffer) + " " * (maxWidth - bLen))
            
        return out
```

---