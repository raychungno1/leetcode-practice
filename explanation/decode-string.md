### Decode String

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

---

<details>
<summary><b>Hint for Optimal Solution</b></summary>
  
This is a recursive descent type of problem. Note that there are 4 types of strings we can encounter - numbers, strings, and brackets - so figure out that do do in each case. Since brackets can be nested, try thinking of a recursive solution. 

</details>

---

<details>
<summary><b>Optimal Solution (Recursive)</b></summary>
  
Since brackets can be nested, e.g. `"3[a2[c]]"`, this problem can be solved recursively. 

At its core, this algorithm treats the incoming string as a buffer of tokens, so we can view `"3[a2[c]]"` as `["3", "[", "a", "2", "[", "c", "]", "]", ]`. We will remove the first token in this buffer, and depending on the type of token, we take a different action. 

On a surface level there are 4 types of "tokens" you will encounter: 
* Number (1-300)
  * Simply store this value
* "[" character
  * Make a recursive call, to parse any nested brackets
  * Once the nested bracket returns, multiply your resulting string by the number stored earlier
* "]" character
  * Return from your recursive call, since this denotes the end of the nested portion
* Alphabetic string
  * Store the string

The recursive function must contain an index variable `i` that is passed into the function, and returned from the function (along with the resulting string) since we are continuously taking elements from our buffer (the input string).

*Time: `O(n)`*
>The algprithm performs a single pass through the input string while parsing the tokens. 

*Space: `O(n)`*
> This problem can make up to `n/4` recursive calls, since a recursive call requires a `x[x]` type input, which has a minimum length of 4. 

```python
class Solution:
    def decodeString(self, s: str) -> str:
        return self.decodeStringRecur(s, 0)[0]
    
    def decodeStringRecur(self, s, i):
        out = ""
        repeat = 0
        while i < len(s):
            # Make recursive call if we see a "["
            # After the call returns, repeat the string
            # the spefified amount
            if s[i] == "[":
                body, i = self.decodeStringRecur(s, i + 1)
                out += repeat * body
                repeat = 0
            
            # Return from recursive call if we see a "]"
            elif s[i] == "]":
                return (out, i + 1)
            
            # Parse digit values 
            elif s[i].isdigit():
                repeat = repeat * 10 + int(s[i])
                i += 1
                
            # Parse string values
            else:
                out += s[i]
                i += 1
                
        # Once we reach end of string
        return out, i
```
</details>

---
<details>
<summary><b>Optimal</b></summary>

To convert from a recursive to an iterative solution, a stack is used. Notice that, when a recursive call is made/returned, the only things that need to be saved is the # of times a string must be repeat, and the current string.

Therefore, we can replace this recursion with a stack, and simply use a for loop to iterate through the characters in the buffer. Start with a stack with 1 element initialized to an empty string. After the loops, our final string will be the last element of the stack. 

* Number (1-300)
  * Simply store this value
* "[" character
  * Push the current repeat number `r` and string `s` to the stack. 
  * Reset the `s` to empty, and `r` to 0
* "]" character
  * Pop the most recent string `s` and most recent repeat number `r` off the stack. 
  * Repeat `s` `r` times, and append the resulting string to the new last element on the stack
  * Reset `r` to 0
* Alphabetic string
  * Store the string



*Time: `O(n)`*
> Same as above.

*Space: `O(n)`*
> Same as above, but instead of recursive calls, we use stack space. 

```python
    def decodeString(self, s: str) -> str:
        stack = [""]
        repeat = 0
        
        for c in s:
            # Store a "recursive" call on the stack
            if c == "[":
                stack.append(repeat)
                stack.append("")
                repeat = 0

            # Recover a "recursive" call, and add it to the current string
            elif c == "]":
                cur = stack.pop()
                repeat = stack.pop()
                stack[-1] += cur * repeat
                repeat = 0  

            # Parse digit values
            elif c.isdigit():
                repeat = repeat * 10 + int(c)

            # Parse string values
            else:
                stack[-1] += c
                
        return stack[-1]
```

---